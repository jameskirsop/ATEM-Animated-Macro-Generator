fps = 50
transition_seconds = 0.4

frames = fps * transition_seconds
template = {
    'start_name':'',
    'end_name':'',
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

def output_frames(math, boxes, i):
    output = ''
    for b,item in boxes.items():
        output = output.__add__(
            f'            <Op id="SuperSourceV2BoxSize" superSource="0" boxIndex="{b}" size="{math[b]["size_func"](a["boxes"][b]["start"]["size"], math[b]["size_range"]/frames*i)}"/>\n'
            f'            <Op id="SuperSourceV2BoxXPosition" superSource="0" boxIndex="{b}" xPosition="{math[b]["xpos_func"](a["boxes"][b]["start"]["xPosition"], math[b]["xpos_range"]/frames*i)}"/>\n'
            f'            <Op id="SuperSourceV2BoxYPosition" superSource="0" boxIndex="{b}" yPosition="{math[b]["ypos_func"](a["boxes"][b]["start"]["yPosition"], math[b]["ypos_range"]/frames*i)}"/>\n'
            f'            <Op id="SuperSourceV2BoxMaskLeft" superSource="0" boxIndex="{b}" left="{math[b]["left_func"](a["boxes"][b]["start"]["left"], math[b]["left_range"]/frames*i)}"/>\n'
            f'            <Op id="SuperSourceV2BoxMaskTop" superSource="0" boxIndex="{b}" top="{math[b]["top_func"](a["boxes"][b]["start"]["top"], math[b]["top_range"]/frames*i)}"/>\n'
            f'            <Op id="SuperSourceV2BoxMaskRight" superSource="0" boxIndex="{b}" right="{math[b]["right_func"](a["boxes"][b]["start"]["right"], math[b]["right_range"]/frames*i)}"/>\n'
            f'            <Op id="SuperSourceV2BoxMaskBottom" superSource="0" boxIndex="{b}" bottom="{math[b]["bottom_func"](a["boxes"][b]["start"]["bottom"], math[b]["bottom_range"]/frames*i)}"/>\n'
        )
    return output

def get_frame_range(frames,reverse):
    if reverse:
        return reversed(range(0,int(frames)+1))
    return range(0,int(frames)+1)
        

animations = []
animations.append({
    'start_name': 'Cam1',
    'end_name': '2Box',
    'fillSource': 'Color2',
    'start_source':'Camera3',
    'end_source':'SuperSource',
    'boxes': {
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
                'xPosition':-5.32,
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

    }
})


output = ''
reverse = False
for index, a in enumerate(animations):
    for reverse in range(0,2):
        if not reverse:
            output += f'        <Macro index="{index}" name="{a["start_name"]} to {a["end_name"]}" description="">\n'
        else:
            output += f'        <Macro index="{index}" name="{a["end_name"]} to {a["start_name"]}" description="">\n'

        for x in range(0,3):
            try:
                output = output.__add__(
                    f'            <Op id="SuperSourceV2BoxEnable" superSource="0" boxIndex="{x}" enable="True"/>\n'
                    f'            <Op id="SuperSourceV2BoxInput" superSource="0" boxIndex="{x}" input="{a["boxes"][x]["source"]}"/>\n'
                )
            except KeyError:
                output = output.__add__(
                f'            <Op id="SuperSourceV2BoxEnable" superSource="0" boxIndex="{x}" enable="False"/>\n'
                )

            output += f'            <Op id="SuperSourceV2ArtFillInput" superSource="0" input="{a["fillSource"]}"/>\n'

        math = {}
        for b,item in a['boxes'].items():
            # print(b)
            math[b] = dict()
            math[b]['size_range'] = abs(item['start']['size'] - item['end']['size'])
            math[b]['size_func'] = lambda a,b: a-b if item['start']['size'] > item['end']['size'] else a+b
            math[b]['xpos_range'] = abs(item['start']['xPosition'] - item['end']['xPosition']) ## if item['start']['xPosition'] > item['end']['xPosition'] else item['start']['xPosition'] + item['end']['xPosition']
            math[b]['xpos_func'] = lambda a,b: a-b if item['start']['xPosition'] > item['end']['xPosition'] else a+b
            math[b]['ypos_range'] = abs(item['start']['yPosition'] - item['end']['yPosition']) ## if item['start']['yPosition'] > item['end']['yPosition'] else item['start']['yPosition'] + item['end']['yPosition']
            math[b]['ypos_func'] = lambda a,b: a-b if item['start']['yPosition'] > item['end']['yPosition'] else a+b
            math[b]['left_range'] = abs(item['start']['left'] - item['end']['left']) ## if item['start']['left'] > item['end']['left'] else item['start']['left'] + item['end']['left']
            math[b]['left_func'] = lambda a,b: a-b if item['start']['left'] > item['end']['left'] else a+b
            math[b]['top_range'] = abs(item['start']['top'] - item['end']['top']) ## if item['start']['top'] > item['end']['top'] else item['start']['top'] + item['end']['top']
            math[b]['top_func'] = lambda a,b: a-b if item['start']['top'] > item['end']['top'] else a+b
            math[b]['right_range'] = abs(item['start']['right'] - item['end']['right']) ## if item['start']['right'] > item['end']['right'] else item['start']['right'] + item['end']['right']
            math[b]['right_func'] = lambda a,b: a-b if item['start']['right'] > item['end']['right'] else a+b
            math[b]['bottom_range'] = abs(item['start']['bottom'] - item['end']['bottom']) ## if item['start']['bottom'] > item['end']['bottom'] else item['start']['bottom'] + item['end']['bottom']
            math[b]['bottom_func'] = lambda a,b: a-b if item['start']['bottom'] > item['end']['bottom'] else a+b

        # import pprint
        # pprint.pprint(math)
        for i in get_frame_range(frames,reverse):
            output += output_frames(math,a['boxes'],i)
            output = output.__add__(f'            <Op id="MacroSleep" frames="1"/>\n')

            ## Change Sources
            if i == 0: #After ensuring that the initial frame has been set to avoid jumping around on frame 1. 
                if not reverse:
                    output = output.__add__(f'            <Op id="ProgramInput" mixEffectBlockIndex="0" input="SuperSource"/>\n')
                else:
                    output = output.__add__(f'            <Op id="ProgramInput" mixEffectBlockIndex="0" input="{a["start_source"]}"/>\n')
                    # Reset the SuperSource to the final position for preview if it's no longer in Program
                    if a["start_source"] != 'SuperSource':
                        output += output_frames(math,a['boxes'],frames)
                output = output.__add__(f'            <Op id="MacroSleep" frames="1"/>\n')
            
            if i == frames:
                if not reverse:
                    output = output.__add__(f'            <Op id="PreviewInput" mixEffectBlockIndex="0" input="{a["start_source"]}"/>\n')
                if reverse:
                    output = output.__add__(f'            <Op id="PreviewInput" mixEffectBlockIndex="0" input="SuperSource"/>\n')

                output = output.__add__(f'            <Op id="MacroSleep" frames="1"/>\n')
            
        output += f'        </Macro>\n'

with open('export.xml','w') as f:
    f.write(output)