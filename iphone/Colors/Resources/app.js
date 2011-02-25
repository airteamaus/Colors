// this sets the background color of the master UIView (when there are no windows/tab groups on it)
//Titanium.UI.setBackgroundColor('#000');
//Titanium.UI.iPhone.statusBarStyle = Titanium.UI.iPhone.StatusBar.OPAQUE_BLACK;

var db = Ti.Database.install('./combos.db', 'colors');

// create tab group
var tabGroup = Titanium.UI.createTabGroup();

//
// create base UI tab and root window
//
var win1 = Titanium.UI.createWindow({  
    title:'Color Palettes',
    backgroundColor:'#fff',
    barColor: '#0a0a0a',
    color: '#9d9896'
});
var tab1 = Titanium.UI.createTab({  
    icon:'KS_nav_views.png',
    title:'All Palettes',
    window:win1
});

/* 
Accepts: An array of strings. Each string is the CSS hex code for a color
Returns: A Titanium.UI.TableViewRow with the combo rendered
*/
create_row_from_combo = function(combo)  // combo is an aray of color values (strings)
{
    //Titanium.API.info('Creating row for: '+ combo);
    var visible_rows = 12;  // Not the actual number displayed, but here for tweaking
    
    var width = Math.round(Titanium.Platform.displayCaps.platformWidth / combo.length);
    var height = Math.round(Titanium.Platform.displayCaps.platformHeight / visible_rows);
    
    var row = Ti.UI.createTableViewRow({
        height: Math.round(height * 1.1),
        borderColor: '#000',
        className: 'combo'
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


get_array_of_combos = function()
{
    Titanium.API.info('Querying the database');
    var iterator = db.execute('SELECT color_id, combo_id FROM combo_color');
    var combos = [];
    while (iterator.isValidRow())
    {
        var combo = parseInt(iterator.fieldByName('combo_id'), 10);
        var color = iterator.fieldByName('color_id');
        if (combos[combo])
        {
            combos[combo].push(color);
        }
        else 
        {
            combos[combo] = [color];
        };
    	iterator.next();
    };
    return combos;    
};


var table = Ti.UI.createTableView({
    backgroundColor:'#000',
    separatorStyle:Ti.UI.iPhone.TableViewSeparatorStyle.NONE
});

Titanium.API.info('Get array of combos ...');
var combos = get_array_of_combos();

Titanium.API.info('Now to make '+ combos.length +' rows from these ...');

for (var i=1; i <= combos.length; i++)
{
    var combo = combos[i];
    var row = combo && create_row_from_combo(combo);
    if ((combo) && (combo.length > 8) && (combo.length < 13))
    {
        //Titanium.API.info('Now to append to the table the row that is combos['+i+']');
        table.appendRow(row);
    };
};

Titanium.API.info('Render the table please ...');
win1.add(table);

//
// create controls tab and root window
//
var win2 = Titanium.UI.createWindow({  
    title:'Favourites',
    backgroundColor:'#fff'
});
var tab2 = Titanium.UI.createTab({  
    icon:'KS_nav_ui.png',
    title:'Favourites',
    window:win2
});

var label2 = Titanium.UI.createLabel({
	color:'#999',
	text:'I am Window 2',
	font:{fontSize:20,fontFamily:'Helvetica Neue'},
	textAlign:'center',
	width:'auto'
});

win2.add(label2);



//
//  add tabs
//
tabGroup.addTab(tab1);  
tabGroup.addTab(tab2);  


// open tab group
tabGroup.open();
