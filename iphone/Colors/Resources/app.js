/*
     ____  _      _          _   _   _     _                       
    |  _ \(_) ___| |__      / \ | |_| | __(_)_ __  ___  ___  _ __  
    | |_) | |/ __| '_ \    / _ \| __| |/ /| | '_ \/ __|/ _ \| '_ \ 
    |  _ <| | (__| | | |  / ___ \ |_|   < | | | | \__ \ (_) | | | |
    |_| \_\_|\___|_| |_| /_/   \_\__|_|\_\|_|_| |_|___/\___/|_| |_|

    Copyright Rich Atkinson 2011 All Rights Reserved
*/

// this sets the background color of the master UIView (when there are no windows/tab groups on it)
//Titanium.UI.setBackgroundColor('#000');
//Titanium.UI.iPhone.statusBarStyle = Titanium.UI.iPhone.StatusBar.OPAQUE_BLACK;

Titanium.API.info('Getting a reference to the DB');
var db = Titanium.Database.install('./combos.db', 'colors');

/* 
Accepts: An array of strings. Each string is the CSS hex code for a color
Returns: A Titanium.UI.TableViewRow with the combo rendered
*/
create_row_from_combo = function(combo, index)  // combo is an aray of color values (strings)
{
    //Titanium.API.info('Creating row for: '+ combo);
    var visible_rows = 12;  // Not the actual number displayed, but here for tweaking
    
    var width = Math.round(Titanium.Platform.displayCaps.platformWidth / combo.length);
    var height = Math.round(Titanium.Platform.displayCaps.platformHeight / visible_rows);
    
    var row = Ti.UI.createTableViewRow({
        height: Math.round(height * 1.1),
        borderColor: '#000',
        className: 'combo',
        path:'./combo.js',
        id: index
    });
    
    var cols = [];
    for (var i=0; i <= combo.length; i++)
    {
        cols[i] = Ti.UI.createView({
           height: height,
           width: width,
           left: width * i,
           backgroundColor: combo[i]
        });  
    };
    row.add(cols);
    return row;
};


/* Query the database. Returns an array of arrays.
*/
get_array_of_combos = function()
{
    Titanium.API.info('Querying the database');
    var iterator = db.execute('SELECT color_id, combo_id FROM combo_color limit 5000');
    //var iterator = db.execute('SELECT combo.reference, combo.id, color.color_id FROM combo, combo_color color WHERE combo.id = color.combo_id;');
    var combos = [];
    while (iterator.isValidRow())
    {
        var combo = parseInt(iterator.fieldByName('combo_id'), 10); //base 10
        var color = iterator.fieldByName('color_id');
        //var reference = iterator.fieldByName('reference');
        if (combos[combo])
        {
            combos[combo].push(color);
        }
        else 
        {
            combos[combo] = [color];
            //index[combo] = reference;
        };
    	iterator.next();
    };
    return combos;
};

// create tab group
var tabGroup = Titanium.UI.createTabGroup();
//
// create base UI tab and root window
//
var win_browse = Titanium.UI.createWindow({  
    title:'Browse',
    backgroundColor:'#fff',
    barColor: '#0a0a0a',
    color: '#9d9896'
});
var tab_browse = Titanium.UI.createTab({  
    icon:'tab_icons/icon_home.png',
    title:'Browse',
    window:win_browse
});

var table_browse = Ti.UI.createTableView({
    backgroundColor:'#000',
    separatorStyle:Ti.UI.iPhone.TableViewSeparatorStyle.NONE
});

Titanium.API.info('Get array of combos ...');
var combos = get_array_of_combos();

Titanium.API.info('Now to make '+ combos.length +' rows from these ...');

for (var i=1; i <= combos.length; i++)
{
    var combo = combos[i];
    var row = combo && create_row_from_combo(combo, i);
    if ((combo) && (combo.length > 8) && (combo.length < 13))
    {
        table_browse.appendRow(row);
    };
};

table_browse.addEventListener('click', function(e)
{
	if (e.rowData.path)
	{
	    // Save button opens an options dialog 
	    var button = Titanium.UI.createButton({
	        //title: 'Options'
	        image: 'nav_icons/icon_download.png'
	    });
	    button.addEventListener('click',function(e)
        {
            // modal options dialog
    	    var options = Titanium.UI.createOptionDialog({
    	        title: 'Palette Options',
                options: ['Download', 'Add to Favourites', 'Like', 'Dislike', 'Cancel'],
                cancel: 4
    	    });
    	    options.show();
        });
        
		var win = Titanium.UI.createWindow({
		    barColor: '#0a0a0a',
			url: e.rowData.path,
			title: 'Palette',
			rightNavButton: button
		});

		var combo = e.rowData.id;
		//Titanium.API.info('Have we got a reference: ' + combo);
		win.combo = combo;
		tab_browse.open(win);
	}
});


Titanium.API.info('Render the table please ...');
win_browse.add(table_browse);
Titanium.API.info('Done.');

//
// Window Favourites
//
var win_favourites = Titanium.UI.createWindow({  
    title:'Favourites',
    backgroundColor:'#fff'
});
var tab_favourites = Titanium.UI.createTab({  
    icon: 'tab_icons/icon_favorites.png',
    title:'Favourites',
    window:win_favourites
});

var label2 = Titanium.UI.createLabel({
	color:'#999',
	text:'I am Window 2',
	font:{fontSize:20,fontFamily:'Helvetica Neue'},
	textAlign:'center',
	width:'auto'
});

win_favourites.add(label2);

//
// Window Random
//
var win_random = Titanium.UI.createWindow({  
    title:'Shuffle',
    backgroundColor:'#fff'
});
var tab_random = Titanium.UI.createTab({  
    icon:'tab_icons/icon_help.png',
    title:'Shuffle',
    window:win_random
});

//
// Window Settings
//
var win_settings = Titanium.UI.createWindow({  
    title:'Settings',
    backgroundColor:'#fff'
});
var tab_settings = Titanium.UI.createTab({  
    icon: 'tab_icons/icon_settings.png',
    title:'Settings',
    window:win_settings
});

//
//  add tabs
//
tabGroup.addTab(tab_browse);  
tabGroup.addTab(tab_random);
tabGroup.addTab(tab_favourites);
tabGroup.addTab(tab_settings);




// open tab group
tabGroup.open();
