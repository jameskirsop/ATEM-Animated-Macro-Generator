# ATEM-Animated-Macro-Generator

This simple python script generates Macros for a BlackMagicDesign ATEM switcher containing animated SuperSource transitions.

The script will generate 2 Macros for each 'animation'. One to transition from the start position to the end, and another for the opposite direction. You can then fire these using the Macros option on your surface, software or using Companion.

The script will output to a file `export.xml` which can be copied and pasted into the appropriate section of an ATEM 'Save As' XML file and then reimported.

Note that you will want to adjust each Macro 'index' if you have Macros already in place on your ATEM. For example:

```
<Macro index="0" name="Cam1 to 2Box" description="">
```

May need to become:
```
<Macro index="22" name="Cam1 to 2Box" description="">
```

You will need python3.7 or higher to run. I've tested on python3.9.

Below is a sample template that you can use to create your macro. Just append this as a new object in the 'animations' list within the script (see sample starting at line 79).
```
{
    'start_name':'CAM3',
    'end_name':'2Box',
    'fillSource':'Color1',
    'start_source':'Camera3',
    'end_source':'SuperSource',
    'boxes':{
        0:{
            'source':'Camera2',
            'start':{
                'size':0.68,
                'xPosition':-27,
                'yPosition':0,
                'left':0,
                'top':0,
                'right':0,
                'bottom':0,
            },
            'end':{
                'size':0.68,
                'xPosition':-27,
                'yPosition':0,
                'left':0,
                'top':0,
                'right':0,
                'bottom':0,
            },
        },
        1:{
            'source':'Camera3',
            'start':{
                'size':1.0,
                'xPosition':0,
                'yPosition':0,
                'left':0,
                'top':0,
                'right':0,
                'bottom':0,
            },
            'end':{
                'size':0.68,
                'xPosition':11,
                'yPosition':0,
                'left':8,
                'top':0,
                'right':8,
                'bottom':0,
                },
        }
    },
}
```