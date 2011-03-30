/*
     ____  _      _          _   _   _     _                       
    |  _ \(_) ___| |__      / \ | |_| | __(_)_ __  ___  ___  _ __  
    | |_) | |/ __| '_ \    / _ \| __| |/ /| | '_ \/ __|/ _ \| '_ \ 
    |  _ <| | (__| | | |  / ___ \ |_|   < | | | | \__ \ (_) | | | |
    |_| \_\_|\___|_| |_| /_/   \_\__|_|\_\|_|_| |_|___/\___/|_| |_|

    Copyright Rich Atkinson 2011 All Rights Reserved
*/

// We don't pass the combo id in, rather we sniff it.
var combo_id = Titanium.UI.currentWindow.combo;

var db = Titanium.Database.install('./combos.db', 'colors');

Titanium.API.info('Show combo '+ combo_id);

// Returns true if the color is dark.
is_dark_color = function(hexcode){
    if (hexcode.length == 6)
    {
        var r = parseInt(hexcode.substr(0,2), 16);
        var g = parseInt(hexcode.substr(2,2), 16);
        var b = parseInt(hexcode.substr(4,2), 16);
        return r+g+b < 256; // darkest 1/3 of colors return true;
    }
    else
    {
        throw "This hexcode isn't a six character string: "+ hexcode;
    };
};



get_table_of_colors = function(combo_id)
{
    /* Query the database. Returns an array of colors. */
    Titanium.API.info('Querying the database');
    //var iterator = db.execute('SELECT combo_id, color_id FROM combo_color WHERE combo_id = ?', combo_id);
    var iterator = db.execute('SELECT combo.reference as reference, combo.id as id, color.color_id as hexcode FROM combo, combo_color color' + 
                              ' WHERE combo.id = color.combo_id AND combo.id = ?', combo_id);
    Titanium.API.info('Returned '+ iterator.rowCount + ' rows');
    var combo = [];
    var table = Ti.UI.createTableView({backgroundColor:'#000', separatorStyle:Ti.UI.iPhone.TableViewSeparatorStyle.NONE});
    while (iterator.isValidRow())
    {
        var id = parseInt(iterator.fieldByName('id'), 10); //base 10
        var hexcode = iterator.fieldByName('hexcode');
        var uuid = iterator.fieldByName('reference');
        
        var text_col = '#000000';
        if (is_dark_color(hexcode))
        {
            text_col = '#ffffff';
        };

        if (combo.indexOf(hexcode) == -1)
        {
            combo.push(hexcode);
            var row = Ti.UI.createTableViewRow({
                borderColor: '#000',
                color: text_col,
                backgroundColor: hexcode,
                uuid: uuid,
                hexcode: hexcode,
                title: '#'+hexcode
            });
            
        };
        table.appendRow(row);
     	iterator.next();
    };
    return table;
};



Titanium.API.info('Get the colors');
var table = get_table_of_colors(combo_id);

Titanium.UI.currentWindow.add(table);



