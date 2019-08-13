#vngame;neo;pool1
# -*- coding: UTF-8 -*-
#-VNFA:BuildFromAutoScriptTemplate-#
# UTF-8 encode is supported now! ^o^

from vnactor import *
from vnframe import *
from vnanime import *

def start(game):
    # use importOrReload to keep vnactor and vnframe updated
    # it is useful if you want to modify vnactor or vnframe script
    from vngameengine import importOrReload
    importOrReload("vnactor")
    importOrReload("vnframe")
    importOrReload("vnanime")
    importOrReload("extplugins")
    
    # enable scene anime function provide by vnframe
    init_scene_anime(game)
    # enable key frame anime function provide by vnanime
    init_keyframe_anime(game)

    # select a skin
    game.skin_set_byname("skin_renpy")

    # enable lip sync provide by vngameengine
    game.isfAutoLipSync = True 
    game.fAutoLipSyncVer = "v11" 
    game.readingSpeed = 12.0
    
    # auto hide and lock style for your game, these are global settings
    game.isHideWindowDuringCameraAnimation = True
    game.isLockWindowDuringSceneAnimation = True
    
    # load scene PNG and then init scene after loaded
    enableQuickReload = False
    game.sceneDir = "pool\\"
    if enableQuickReload and hasattr(game, "scenePNG") and game.scenePNG == "pool1.png":
        # skip load png, quick reload
        # all actor/prop status must be reset by script
        init_scene(game)
    else:
        load_and_init_scene(game, "pool1.png", init_scene)
    
def init_scene(game):
    try:
        # show our game window
        game.visible = 1
        game.isHideGameButtons = 0
        
        # load actor/prop/string from scene by "tag folder", must be called after scene is loaded
        register_actor_prop_by_tag(game)
        register_string_resource(game)
        
        # import clips, after actor/prop registered
        for clip in keyframeClips:
            kfa_import(game, clip)

        # init script helper, must be called after actor/prop registered
        sh = init_script_helper(game)
        sh.createLocalizeStringOnBuild = False
        sh.masterMode = False
        sh.baseNest = "        " # base nest space of dumpped script
        sh.nestWord = "    " # space inserted when script is nested
        sh.load_python() # load this python file for auto script
        sh.asEnable = True # enable auto script feature
        
        # setup default next button
        game.btnNextText = "Next >>"

        # here game start
        toSeq1(game)

    except Exception as e:
        import traceback
        traceback.print_exc()
        toEnd(game, "init_scene FAILED: "+str(e))

def toSeq1(game):
    game.texts_next([
        #-VNFA:seq:start:1-#
        ["s", "Scene 2 Start", act, {
            'cam': {'goto_pos': ((-6.472, 7.909, 11.925), (0.000, 0.000, -2.632), (9.500, -33.100, 0.000))},
            'wineglass': {'fk_set': ((0.000, 0.000, 0.000), (0.000, 0.000, 0.000), (0.000, 0.000, 0.000)), 'move_to': (0.001, -0.009, -0.008), 'rotate_to': (60.183, 256.142, 261.990), 'scale_to': (0.800, 0.800, 0.800), 'visible': 1},
            'Nia': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (1, 4, 4), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.000, 'cloth_all': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 'cloth_type': 2, 'eyes': 0, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAAD6//+xMbT9vfr//7A0B34/+PgoPQQilL5+fkw8hs10Pw==', 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {}, 'hands': (0, 11), 'ik_active': (0, 0, 0, 1, 0), 'ik_set': {'cf_J_ArmLow01_R': ((0.202, 0.725, -0.065), ), 'cf_J_ArmUp00_R': ((0.114, 0.952, -0.052), ), 'cf_J_Hand_R': ((0.157, 0.813, 0.149), (276.455, 137.000, 144.860))}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 1, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 1, 'mouth_open': 0.000, 'move_to': (-7.380, 7.034, 12.894), 'nip_stand': 0.000, 'rotate_to': (0.000, 168.685, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'bottle': {'fk_set': ((0.000, 0.000, 0.000), ), 'move_to': (-6.959, 7.819, 11.969), 'rotate_to': (0.000, 271.132, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'visible': 1},
            'sys': {'bg_png': 'sample01.png', 'bgm': (0, 0), 'env': (0, 0), 'map': -1, 'map_pos': (0.000, 0.000, 0.000), 'map_rot': (0.000, 0.000, 0.000), 'wav': ('', 0, 1)},
            'Me': {'acc_all': (0, 0, 0, 0, 0, 1, 1, 1, 1, 1), 'anim': (1, 4, 0), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.000, 'cloth_all': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 'cloth_type': 2, 'eyes': 0, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAAABAACyqzs7PgEAoLEur3s/dWk2vWgBqD4kxn08JIZxPw==', 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 1, 'mouth_open': 0.000, 'move_to': (-6.493, 7.058, 12.439), 'nip_stand': 0.000, 'rotate_to': (0.000, 231.030, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
        }],
        ["Nia", "Thank you for bringing my purse, that was very gentleman like of you.", act, {
            'cam': {'goto_pos': ((-6.788, 7.843, 12.430), (0.000, 0.000, -2.632), (2.400, -42.050, 0.000))},
            'wineglass': {'fk_set': ((0.000, 0.000, 0.000), (0.000, 0.000, 0.000), (0.000, 0.000, 0.000)), 'move_to': (0.001, -0.009, -0.008), 'rotate_to': (60.183, 256.142, 261.990), 'scale_to': (0.800, 0.800, 0.800), 'visible': 1},
            'Nia': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (1, 4, 4), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.000, 'cloth_all': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 'cloth_type': 2, 'eyes': 0, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAAD6//+xMbT9vfr//7A0B34/+PgoPQQilL5+fkw8hs10Pw==', 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {}, 'hands': (0, 11), 'ik_active': (0, 0, 0, 1, 0), 'ik_set': {'cf_J_ArmLow01_R': ((0.202, 0.725, -0.065), ), 'cf_J_ArmUp00_R': ((0.114, 0.952, -0.052), ), 'cf_J_Hand_R': ((0.157, 0.813, 0.149), (276.455, 137.000, 144.860))}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 1, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 1, 'mouth_open': 0.000, 'move_to': (-7.380, 7.034, 12.894), 'nip_stand': 0.000, 'rotate_to': (0.000, 168.685, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'bottle': {'fk_set': ((0.000, 0.000, 0.000), ), 'move_to': (-6.959, 7.819, 11.969), 'rotate_to': (0.000, 271.132, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'visible': 1},
            'sys': {'bg_png': 'sample01.png', 'bgm': (0, 0), 'env': (0, 0), 'map': -1, 'map_pos': (0.000, 0.000, 0.000), 'map_rot': (0.000, 0.000, 0.000), 'wav': ('', 0, 1)},
            'Me': {'acc_all': (0, 0, 0, 0, 0, 1, 1, 1, 1, 1), 'anim': (1, 4, 0), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.000, 'cloth_all': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 'cloth_type': 2, 'eyes': 0, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAAABAACyqzs7PgEAoLEur3s/dWk2vWgBqD4kxn08JIZxPw==', 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 1, 'mouth_open': 0.000, 'move_to': (-6.493, 7.058, 12.439), 'nip_stand': 0.000, 'rotate_to': (0.000, 231.030, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
        }],
        ["Me", "No problem.", act, {
            'cam': {'goto_pos': ((-7.329, 7.842, 12.586), (0.000, 0.000, -2.677), (10.550, 95.650, 0.000))},
        }],
        ["Nia", "So, you're here with your family?", act, {
            'cam': {'goto_pos': ((-6.788, 7.843, 12.430), (0.000, 0.000, -2.632), (2.400, -42.050, 0.000))},
        }],
        ["Me", "Yes, on vacation. Are you on vacation too?", act, {
            'cam': {'goto_pos': ((-7.329, 7.842, 12.586), (0.000, 0.000, -2.677), (10.550, 95.650, 0.000))},
        }],
        ["Nia", "No, I actually work here at the hotel. I'm the bar manager down there by the pool", act, {
            'cam': {'goto_pos': ((-6.788, 7.843, 12.430), (0.000, 0.000, -2.632), (2.400, -42.050, 0.000))},
        }],
        ["Me", "Do you like it?", act, {
            'cam': {'goto_pos': ((-7.329, 7.842, 12.586), (0.000, 0.000, -2.677), (10.550, 95.650, 0.000))},
        }],
        ["s", "Nia takes a sip from her wine.", act, {
            'Nia': {'eyes_open': 0.684, 'face_to_full2': 'BAAAAAIAAAD88fm7/P//rQAAAAAY/n8/QUZXvo6lOT6loyI9Vrp1Pw==', 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (-39.494, 18.568, -1.747), 2: (4.491, -3.889, 0.979)}, 'ik_set': {'cf_J_ArmLow01_R': ((0.202, 0.725, -0.065), ), 'cf_J_ArmUp00_R': ((0.114, 0.952, -0.052), ), 'cf_J_Hand_R': ((0.123, 1.062, 0.139), (2.062, 211.557, 96.340))}, 'kinematic': 3, 'mouth': 0, 'mouth_open': 0.382},
            'cam': {'goto_pos': ((-7.165, 7.893, 12.742), (0.000, 0.000, -2.640), (-0.300, -49.100, 0.000))},
            'wineglass': {'rotate_to': (60.183, 256.142, 256.533)},
        }],
        ["Nia", "Yes, it's a wonderful place to be. It's always warm and sunny, really great.", act, {
            'Nia': {'eyes_open': 1.000, 'face_to_full2': 'BAAAAAIAAAD8/4e01gqgvfr/x7KWN38/C4EQPXn7rr5zXlI8rWRwPw==', 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {}, 'ik_set': {'cf_J_ArmLow01_R': ((0.202, 0.725, -0.065), ), 'cf_J_ArmUp00_R': ((0.114, 0.952, -0.052), ), 'cf_J_Hand_R': ((0.157, 0.813, 0.149), (276.455, 137.000, 144.860))}, 'kinematic': 1, 'look_at_ptn': 3, 'mouth': 1, 'mouth_open': 0.000, 'rotate_to': (0.000, 168.685, 0.000)},
            'cam': {'goto_pos': ((-6.788, 7.843, 12.430), (0.000, 0.000, -2.632), (2.400, -42.050, 0.000))},
        }],
        ["Nia", "Only some of the guests get really annoying...", act, {
            'cam': {'goto_pos': ((-7.928, 8.006, 13.425), (0.000, 0.000, -2.620), (-1.100, -51.100, 0.000))},
        }],
        ["Me", "You mean those bozos talking to you all the time?", act, {
            'cam': {'goto_pos': ((-6.128, 7.808, 12.479), (0.000, 0.000, -2.702), (9.600, 104.050, 0.000))},
        }],
        ["Nia", "Exactly. So you've noticed? Ugh, they are so stupid, trying to impress me with their large... abs. And how much they can weightlift.", act, {
            'cam': {'goto_pos': ((-7.728, 8.023, 13.171), (0.000, 0.000, -2.697), (-2.800, -50.350, 0.000))},
        }],
        ["Me", "That doesn't sound very interesting.", act, {
            'cam': {'goto_pos': ((-6.128, 7.808, 12.479), (0.000, 0.000, -2.702), (9.650, 104.100, 0.000))},
        }],
        ["Nia", "Haha, it's not, but they think it is.", act, {
            'cam': {'goto_pos': ((-7.728, 8.023, 13.171), (0.000, 0.000, -2.697), (-2.800, -50.350, 0.000))},
        }],
        ["Me", "I heard them talking about you.", act, {
            'cam': {'goto_pos': ((-6.128, 7.808, 12.479), (0.000, 0.000, -2.702), (9.600, 104.100, 0.000))},
        }],
        ["Nia", "Oh, what did they say?", act, {
            'Nia': {'eyes': 3, 'eyes_open': 0.853, 'mouth': 0},
            'cam': {'goto_pos': ((-8.392, 8.065, 13.534), (0.000, 0.000, -2.710), (-0.900, -55.600, 0.000))},
        }],
        ["s", "The boy realized he was treading on thin ice.", act, {
            'cam': {'goto_pos': ((-6.128, 7.808, 12.479), (0.000, 0.000, -2.702), (9.600, 104.100, 0.000))},
        }],
        ["Me", "Stupid things, about... you know... doing things with you. They think you're some kind of trophy.", act, {
            'cam': {'goto_pos': ((-6.128, 7.808, 12.479), (0.000, 0.000, -2.702), (9.550, 104.050, 0.000))},
        }],
        ["Nia", "And what do you think?", act, {
            'Nia': {'eyes': 0, 'eyes_open': 1.000},
            'cam': {'goto_pos': ((-7.728, 8.023, 13.171), (0.000, 0.000, -2.697), (-2.800, -50.350, 0.000))},
        }],
        ["s", "<sip>", act, {
            'Nia': {'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (-39.494, 18.568, -1.747), 2: (4.491, -3.889, 0.979)}, 'ik_set': {'cf_J_ArmLow01_R': ((0.202, 0.725, -0.065), ), 'cf_J_ArmUp00_R': ((0.114, 0.952, -0.052), ), 'cf_J_Hand_R': ((0.123, 1.062, 0.139), (2.062, 211.557, 96.340))}, 'kinematic': 3},
            'cam': {'goto_pos': ((-7.728, 8.023, 13.171), (0.000, 0.000, -2.697), (-2.800, -50.350, 0.000))},
        }],
        ["Me", "I think you're really pretty and nice. And that they should shut their mouths.", act, {
            'Nia': {'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {}, 'ik_set': {'cf_J_ArmLow01_R': ((0.202, 0.725, -0.065), ), 'cf_J_ArmUp00_R': ((0.114, 0.952, -0.052), ), 'cf_J_Hand_R': ((0.157, 0.813, 0.149), (276.455, 137.000, 144.860))}, 'kinematic': 1, 'mouth': 1},
            'cam': {'goto_pos': ((-6.128, 7.808, 12.479), (0.000, 0.000, -2.702), (9.600, 104.100, 0.000))},
        }],
        ["Nia", "Oh, pretty eh? How pretty?", act, {
            'Nia': {'face_red': 0.279},
            'Me': {'face_red': 0.118},
            'cam': {'goto_pos': ((-7.728, 8.023, 13.171), (0.000, 0.000, -2.697), (-2.800, -50.350, 0.000))},
        }],
        ["s", "The boy was at a loss for words.", act, {
            'Nia': {'eyes_open': 0.000, 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (-39.494, 18.568, -1.747), 2: (4.491, -3.889, 0.979)}, 'ik_set': {'cf_J_ArmLow01_R': ((0.202, 0.725, -0.065), ), 'cf_J_ArmUp00_R': ((0.114, 0.952, -0.052), ), 'cf_J_Hand_R': ((0.123, 1.062, 0.139), (2.062, 211.557, 96.340))}, 'kinematic': 3},
            'Me': {'eyes': 1, 'mouth': 0, 'mouth_open': 0.360},
            'cam': {'goto_pos': ((-6.769, 7.789, 12.771), (0.000, 0.000, -2.705), (14.950, 87.600, 0.000))},
        }],
        ["Nia", "Huh?!", act, {
            'Nia': {'eyes_open': 1.000, 'ik_set': {'cf_J_ArmLow01_R': ((0.202, 0.725, -0.065), ), 'cf_J_ArmUp00_R': ((0.114, 0.952, -0.052), ), 'cf_J_Hand_R': ((0.193, 0.978, 0.223), (330.603, 207.742, 97.277))}, 'mouth': 0, 'mouth_open': 0.397},
            'Me': {'anim': (1, 3, 21), 'eyes_open': 0.000, 'face_to_full2': 'BAAAAAIAAAD8//+wX0TbuwAAAACI/n8//qgcupVF27v+P4a2hv5/Pw==', 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (-40.413, 16.799, -11.074), 2: (-30.854, 17.142, -8.989)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.196, 0.914, -0.169), ), 'cf_J_ArmLow01_R': ((0.132, 0.926, -0.201), ), 'cf_J_ArmUp00_L': ((-0.061, 0.993, 0.113), ), 'cf_J_ArmUp00_R': ((0.113, 0.977, 0.023), ), 'cf_J_Foot01_L': ((-0.059, 0.064, -0.172), (359.643, 4.123, 0.628)), 'cf_J_Foot01_R': ((0.038, 0.063, -0.196), (359.742, 7.016, 359.448)), 'cf_J_Hand_L': ((-0.107, 0.688, -0.035), (300.566, 123.824, 19.090)), 'cf_J_Hand_R': ((0.043, 0.700, -0.037), (293.904, 248.714, 324.503)), 'cf_J_Hips': ((-0.007, 0.828, -0.087), ), 'cf_J_LegLow01_L': ((-0.071, 0.416, -0.127), ), 'cf_J_LegLow01_R': ((0.041, 0.416, -0.146), ), 'cf_J_LegUp00_L': ((-0.093, 0.686, -0.135), ), 'cf_J_LegUp00_R': ((0.030, 0.693, -0.167), )}, 'kinematic': 3, 'mouth': 24, 'mouth_open': 0.000, 'move_to': (-7.153, 7.058, 12.781), 'rotate_to': (0.000, 259.783, 0.000)},
            'cam': {'goto_pos': ((-6.748, 7.663, 13.379), (0.000, 0.000, -2.985), (20.600, 49.650, 0.000))},
        }],
        ["Me", "I'm sorry, I shouldn't have done that.", act, {
            'Nia': {'face_to_full2': 'BAAAAAIAAAD9/z+yuEhBvv3/P7L1ZXs/wrPdvbPyrb61YiG9tfVuPw==', 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {}, 'ik_set': {'cf_J_ArmLow01_R': ((0.202, 0.725, -0.065), ), 'cf_J_ArmUp00_R': ((0.114, 0.952, -0.052), ), 'cf_J_Hand_R': ((0.157, 0.813, 0.149), (276.455, 137.000, 144.860))}, 'kinematic': 1},
            'Me': {'eyes_open': 1.000, 'face_to_full2': 'BAAAAAIAAAABAACx0HvXugEAgLDq/38/MlpUPR6jvD2hW527JJB+Pw==', 'fk_set': {}, 'ik_set': {}, 'kinematic': 0, 'look_at_ptn': 3, 'mouth': 6},
            'cam': {'goto_pos': ((-6.279, 8.163, 13.108), (0.000, 0.000, -2.825), (-6.100, 76.900, 0.000))},
        }],
        ["Nia", "No, it's ok, that was really sweet of you. I was just surprised.", act, {
            'Nia': {'eyes': 1, 'mouth': 1, 'mouth_open': 0.000},
            'cam': {'goto_pos': ((-8.883, 7.743, 14.172), (0.000, 0.000, -3.005), (11.850, -49.750, 0.000))},
        }],
        ["Nia", "Look I'll give you one too.", act, {
            'cam': {'goto_pos': ((-8.883, 7.743, 14.172), (0.000, 0.000, -3.005), (11.850, -49.750, 0.000))},
        }],
        ["s", "<smooch>", act, {
            'Nia': {'eyes_open': 0.000, 'fk_set': {1: (-51.826, -46.314, 6.095), 2: (21.248, -3.549, 1.432), 9: (-0.916, -0.027, 0.027), 13: (-3.917, -0.877, 0.846)}, 'hands': (0, 17), 'kinematic': 3, 'mouth': 21},
            'Me': {'fk_set': {1: (-29.475, -50.543, 30.873), 2: (-30.854, 17.142, -8.989)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.196, 0.914, -0.169), ), 'cf_J_ArmLow01_R': ((0.132, 0.926, -0.201), ), 'cf_J_ArmUp00_L': ((-0.074, 0.995, 0.074), ), 'cf_J_ArmUp00_R': ((0.070, 0.872, -0.056), ), 'cf_J_Foot01_L': ((-0.059, 0.064, -0.172), (359.643, 4.123, 0.628)), 'cf_J_Foot01_R': ((0.038, 0.063, -0.196), (359.742, 7.016, 359.448)), 'cf_J_Hand_L': ((-0.107, 0.688, -0.035), (300.566, 123.824, 19.090)), 'cf_J_Hand_R': ((0.043, 0.700, -0.037), (293.904, 248.714, 324.503)), 'cf_J_Hips': ((-0.007, 0.828, -0.087), ), 'cf_J_LegLow01_L': ((-0.071, 0.416, -0.127), ), 'cf_J_LegLow01_R': ((0.041, 0.416, -0.146), ), 'cf_J_LegUp00_L': ((-0.093, 0.686, -0.135), ), 'cf_J_LegUp00_R': ((0.030, 0.693, -0.167), )}, 'kinematic': 3, 'mouth': 1},
            'cam': {'goto_pos': ((-6.530, 7.880, 13.866), (0.000, 0.000, -2.885), (9.550, 38.950, 0.000))},
        }],
        ["Nia", "Nnnggg", act, {
            'Nia': {'anim_spd': 0.000, 'eyes': 11, 'eyes_open': 1.000},
            'Me': {'anim_spd': 0.000, 'fk_set': {1: (-38.430, 13.004, -38.018), 2: (-30.364, 23.668, -7.678)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.196, 0.914, -0.169), ), 'cf_J_ArmLow01_R': ((0.132, 0.926, -0.201), ), 'cf_J_ArmUp00_L': ((-0.108, 0.972, 0.050), ), 'cf_J_ArmUp00_R': ((0.079, 0.881, -0.050), ), 'cf_J_Foot01_L': ((-0.059, 0.064, -0.172), (359.643, 4.123, 0.628)), 'cf_J_Foot01_R': ((0.038, 0.063, -0.196), (359.742, 7.016, 359.448)), 'cf_J_Hand_L': ((-0.107, 0.688, -0.035), (300.566, 123.824, 19.090)), 'cf_J_Hand_R': ((0.043, 0.700, -0.037), (293.904, 248.714, 324.503)), 'cf_J_Hips': ((-0.007, 0.828, -0.087), ), 'cf_J_LegLow01_L': ((-0.071, 0.416, -0.127), ), 'cf_J_LegLow01_R': ((0.041, 0.416, -0.146), ), 'cf_J_LegUp00_L': ((-0.093, 0.686, -0.135), ), 'cf_J_LegUp00_R': ((0.030, 0.693, -0.167), )}, 'mouth': 22},
            'cam': {'goto_pos': ((-7.308, 7.691, 14.127), (0.000, 0.000, -2.795), (15.100, 0.550, 0.000))},
        }],
        ["s", "Nia looked a bit sad.", act, {
            'Nia': {'eyes': 2, 'fk_set': {1: (-19.110, -42.821, 3.982), 2: (-3.717, 11.139, 0.371), 9: (-0.916, -0.027, 0.027), 13: (-3.917, -0.877, 0.846)}, 'mouth': 0},
            'Me': {'fk_set': {1: (-11.594, -6.423, -9.268), 2: (-30.364, 23.668, -7.678)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.196, 0.914, -0.169), ), 'cf_J_ArmLow01_R': ((0.132, 0.926, -0.201), ), 'cf_J_ArmUp00_L': ((-0.138, 0.966, -0.025), ), 'cf_J_ArmUp00_R': ((0.068, 0.892, -0.089), ), 'cf_J_Foot01_L': ((-0.059, 0.064, -0.172), (359.643, 4.123, 0.628)), 'cf_J_Foot01_R': ((0.038, 0.063, -0.196), (359.742, 7.016, 359.448)), 'cf_J_Hand_L': ((-0.107, 0.688, -0.035), (300.566, 123.824, 19.090)), 'cf_J_Hand_R': ((0.043, 0.700, -0.037), (293.904, 248.714, 324.503)), 'cf_J_Hips': ((-0.010, 0.835, -0.100), ), 'cf_J_LegLow01_L': ((-0.071, 0.416, -0.127), ), 'cf_J_LegLow01_R': ((0.041, 0.416, -0.146), ), 'cf_J_LegUp00_L': ((-0.093, 0.686, -0.135), ), 'cf_J_LegUp00_R': ((0.030, 0.693, -0.167), )}, 'mouth': 1},
            'cam': {'goto_pos': ((-7.655, 7.746, 14.118), (0.000, 0.000, -2.697), (16.950, -14.350, 0.000))},
        }],
        ["Nia", "Not on the mouth.", act, {
            'cam': {'goto_pos': ((-7.635, 7.745, 14.017), (0.000, 0.000, -2.697), (16.550, -16.200, 0.000))},
        }],
        ["Me", "But it was so nice.", act, {
            'cam': {'goto_pos': ((-5.994, 7.986, 13.020), (0.000, 0.000, -2.795), (4.250, 82.400, 0.000))},
        }],
        ["Nia", "It's not okay to just kiss someone on the lips.", act, {
            'Nia': {'face_red': 0.529},
            'cam': {'goto_pos': ((-7.698, 7.717, 14.053), (0.000, 0.000, -2.787), (16.500, -17.800, 0.000))},
        }],
        ["s", "The boy thinking this was some a fun game, said:", act, {
            'cam': {'goto_pos': ((-5.994, 7.986, 13.020), (0.000, 0.000, -2.795), (4.200, 82.400, 0.000))},
        }],
        ["Me", "Ok, on the cheeks then.", act, {
            'cam': {'goto_pos': ((-5.994, 7.986, 13.020), (0.000, 0.000, -2.795), (4.200, 82.400, 0.000))},
        }],
        ["s", "The boy leaned forward.", act, {
            'Nia': {'eyes': 1, 'face_red': 0.449, 'fk_set': {1: (-51.859, -45.802, 5.693), 2: (21.248, -3.549, 1.432), 9: (-0.916, -0.027, 0.027), 13: (-3.917, -0.877, 0.846)}, 'mouth': 1},
            'Me': {'fk_set': {1: (-23.480, 0.932, -31.737), 2: (-34.508, 24.346, -8.042)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.196, 0.914, -0.169), ), 'cf_J_ArmLow01_R': ((0.132, 0.926, -0.201), ), 'cf_J_ArmUp00_L': ((-0.083, 0.997, 0.016), ), 'cf_J_ArmUp00_R': ((0.079, 0.881, -0.050), ), 'cf_J_Foot01_L': ((-0.059, 0.064, -0.172), (359.643, 4.123, 0.628)), 'cf_J_Foot01_R': ((0.038, 0.063, -0.196), (359.742, 7.016, 359.448)), 'cf_J_Hand_L': ((-0.107, 0.688, -0.035), (300.566, 123.824, 19.090)), 'cf_J_Hand_R': ((0.043, 0.700, -0.037), (293.904, 248.714, 324.503)), 'cf_J_Hips': ((-0.007, 0.828, -0.087), ), 'cf_J_LegLow01_L': ((-0.071, 0.416, -0.127), ), 'cf_J_LegLow01_R': ((0.041, 0.416, -0.146), ), 'cf_J_LegUp00_L': ((-0.093, 0.686, -0.135), ), 'cf_J_LegUp00_R': ((0.030, 0.693, -0.167), )}, 'mouth': 22},
            'cam': {'goto_pos': ((-7.361, 7.552, 14.314), (0.000, 0.000, -2.795), (20.700, -2.950, 0.000))},
        }],
        ["s", "They boy shifted suddenly and kissed her lips again. This time holding the kiss longer.", act, {
            'Nia': {'eyes': 9, 'face_red': 0.279, 'fk_set': {1: (-51.826, -46.314, 6.095), 2: (21.248, -3.549, 1.432), 9: (-0.916, -0.027, 0.027), 13: (-3.917, -0.877, 0.846)}, 'mouth': 0},
            'Me': {'fk_set': {1: (-38.430, 13.004, -38.018), 2: (-30.364, 23.668, -7.678)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.196, 0.914, -0.169), ), 'cf_J_ArmLow01_R': ((0.132, 0.926, -0.201), ), 'cf_J_ArmUp00_L': ((-0.106, 0.971, 0.053), ), 'cf_J_ArmUp00_R': ((0.079, 0.881, -0.051), ), 'cf_J_Foot01_L': ((-0.059, 0.064, -0.172), (359.643, 4.123, 0.628)), 'cf_J_Foot01_R': ((0.038, 0.063, -0.196), (359.742, 7.016, 359.448)), 'cf_J_Hand_L': ((-0.107, 0.688, -0.035), (300.566, 123.824, 19.090)), 'cf_J_Hand_R': ((0.043, 0.700, -0.037), (293.904, 248.714, 324.503)), 'cf_J_Hips': ((-0.007, 0.828, -0.087), ), 'cf_J_LegLow01_L': ((-0.071, 0.416, -0.127), ), 'cf_J_LegLow01_R': ((0.041, 0.416, -0.146), ), 'cf_J_LegUp00_L': ((-0.093, 0.686, -0.135), ), 'cf_J_LegUp00_R': ((0.030, 0.693, -0.167), )}},
            'cam': {'goto_pos': ((-7.326, 7.724, 14.295), (0.000, 0.000, -2.727), (15.850, 0.300, 0.000))},
        }],
        ["s", "He expected her to pull away, but suddenly she gripped him and kissed him back intensely", act, {
            'Nia': {'anim': (3, 33, 1), 'anim_spd': 0.309, 'eyes_open': 0.000, 'fk_set': {1: (-47.219, -46.746, -0.317), 2: (21.248, -3.549, 6.540), 9: (-0.916, -0.027, 0.027), 13: (-3.917, -0.877, 0.846)}, 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {'cf_J_ArmLow01_L': ((-0.168, 0.812, -0.131), ), 'cf_J_ArmLow01_R': ((0.202, 0.725, -0.065), ), 'cf_J_ArmUp00_L': ((-0.111, 0.950, -0.014), ), 'cf_J_ArmUp00_R': ((0.114, 0.952, -0.052), ), 'cf_J_Foot01_L': ((-0.041, 0.077, 0.451), (359.638, 3.402, 0.272)), 'cf_J_Foot01_R': ((-0.179, 0.326, 0.505), (8.556, 325.566, 340.881)), 'cf_J_Hand_L': ((-0.232, 1.093, 0.088), (301.991, 208.080, 262.484)), 'cf_J_Hand_R': ((0.157, 0.813, 0.149), (276.455, 137.000, 144.860)), 'cf_J_Hips': ((0.000, 0.650, 0.007), ), 'cf_J_LegLow01_L': ((0.029, 0.499, 0.398), ), 'cf_J_LegLow01_R': ((0.009, 0.682, 0.352), ), 'cf_J_LegUp00_L': ((-0.082, 0.502, 0.028), ), 'cf_J_LegUp00_R': ((0.080, 0.500, 0.018), )}, 'mouth': 25},
            'Me': {'anim': (3, 33, 1), 'anim_spd': 0.375, 'fk_set': {1: (-12.353, 13.505, -66.422), 2: (-33.872, 33.630, -4.846)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.196, 0.914, -0.169), ), 'cf_J_ArmLow01_R': ((0.132, 0.926, -0.201), ), 'cf_J_ArmUp00_L': ((-0.102, 0.981, 0.060), ), 'cf_J_ArmUp00_R': ((0.075, 0.880, -0.055), ), 'cf_J_Foot01_L': ((-0.059, 0.064, -0.172), (359.643, 4.123, 0.628)), 'cf_J_Foot01_R': ((0.038, 0.063, -0.196), (359.742, 7.016, 359.448)), 'cf_J_Hand_L': ((-0.107, 0.688, -0.035), (300.566, 123.824, 19.090)), 'cf_J_Hand_R': ((0.043, 0.700, -0.037), (293.904, 248.714, 324.503)), 'cf_J_Hips': ((-0.002, 0.833, -0.084), ), 'cf_J_LegLow01_L': ((-0.071, 0.416, -0.127), ), 'cf_J_LegLow01_R': ((0.041, 0.416, -0.146), ), 'cf_J_LegUp00_L': ((-0.093, 0.686, -0.135), ), 'cf_J_LegUp00_R': ((0.030, 0.693, -0.167), )}, 'mouth': 0, 'mouth_open': 1.000},
            'cam': {'goto_pos': ((-7.363, 8.000, 14.398), (0.000, 0.000, -2.532), (5.850, -0.200, 0.000))},
        }],
        ["s", "It was his first real kiss and it was amazing.", act, {
            'Me': {'eyes_open': 0.000},
            'cam': {'goto_pos': ((-5.970, 7.868, 14.045), (0.000, 0.000, -2.532), (8.500, 47.750, 0.000))},
        }],
        ["s", "They kissed for a long time.", act, {
            'Nia': {'face_red': 0.654},
            'Me': {'face_red': 0.625},
            'cam': {'goto_pos': ((-7.389, 7.097, 14.133), (0.000, 0.000, -2.310), (39.750, -1.350, 0.000))},
        }],
        ["Nia", "Did you like that?", act, {
            'Nia': {'anim': (1, 4, 4), 'anim_spd': 0.860, 'eyes': 2, 'eyes_open': 1.000, 'face_red': 0.279, 'fk_set': {1: (-19.110, -42.821, 3.982), 2: (-3.717, 11.139, 0.371), 9: (-0.916, -0.027, 0.027), 13: (-3.917, -0.877, 0.846)}, 'ik_active': (0, 0, 0, 1, 0), 'ik_set': {'cf_J_ArmLow01_R': ((0.202, 0.725, -0.065), ), 'cf_J_ArmUp00_R': ((0.114, 0.952, -0.052), ), 'cf_J_Hand_R': ((0.157, 0.813, 0.149), (276.455, 137.000, 144.860))}, 'mouth': 0},
            'Me': {'anim': (1, 4, 4), 'anim_spd': 0.662, 'eyes_open': 1.000, 'face_red': 0.676, 'fk_set': {1: (-11.594, -6.423, -9.268), 2: (-30.364, 23.668, -7.678)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.196, 0.914, -0.169), ), 'cf_J_ArmLow01_R': ((0.132, 0.926, -0.201), ), 'cf_J_ArmUp00_L': ((-0.138, 0.966, -0.025), ), 'cf_J_ArmUp00_R': ((0.068, 0.892, -0.089), ), 'cf_J_Foot01_L': ((-0.059, 0.064, -0.172), (359.643, 4.123, 0.628)), 'cf_J_Foot01_R': ((0.038, 0.063, -0.196), (359.742, 7.016, 359.448)), 'cf_J_Hand_L': ((-0.107, 0.688, -0.035), (300.566, 123.824, 19.090)), 'cf_J_Hand_R': ((0.043, 0.700, -0.037), (293.904, 248.714, 324.503)), 'cf_J_Hips': ((-0.010, 0.835, -0.100), ), 'cf_J_LegLow01_L': ((-0.071, 0.416, -0.127), ), 'cf_J_LegLow01_R': ((0.041, 0.416, -0.146), ), 'cf_J_LegUp00_L': ((-0.093, 0.686, -0.135), ), 'cf_J_LegUp00_R': ((0.030, 0.693, -0.167), )}, 'mouth': 1, 'mouth_open': 0.000},
            'cam': {'goto_pos': ((-7.642, 7.555, 14.336), (0.000, 0.000, -2.987), (19.700, -14.450, 0.000))},
        }],
        ["Me", "Yes! That was the best thing ever! Can we do it again?", act, {
            'Me': {'fk_set': {1: (-10.987, -2.772, -9.983), 2: (-19.080, 22.070, -7.006)}},
            'cam': {'goto_pos': ((-6.001, 8.042, 13.156), (0.000, 0.000, -2.822), (2.600, 78.150, 0.000))},
        }],
        ["s", "Nia looked down towards the pool, checking if someone was watching.", act, {
            'Nia': {'fk_set': {1: (2.420, -19.339, 0.537), 2: (-3.717, 11.139, 0.371), 9: (-0.916, -0.027, 0.027), 13: (-3.917, -0.877, 0.846)}, 'look_at_ptn': 1},
            'cam': {'goto_pos': ((-7.224, 7.927, 11.967), (0.000, 0.000, -2.780), (-7.250, 0.150, 0.000))},
        }],
        ["s", "Nia stood up.", act, {
            'Nia': {'fk_set': {1: (-19.110, -42.821, 3.982), 2: (-3.717, 11.139, 0.371), 9: (-0.916, -0.027, 0.027), 13: (-3.917, -0.877, 0.846)}, 'look_at_ptn': 3, 'mouth': 1},
            'cam': {'goto_pos': ((-7.673, 7.872, 14.379), (0.000, 0.000, -2.862), (9.600, -11.450, 0.000))},
        }],
        #-VNFA:seq:end:1-#
    ], toSeq2)

def toSeq2(game):
    game.texts_next([
        #-VNFA:seq:start:2-#
        ["Nia", "Well, are you coming in?", act, {
            'Nia': {'anim': (2, 13, 4), 'anim_spd': 0.860, 'eyes': 2, 'face_red': 0.279, 'face_to_full2': 'BAAAAAIAAAD9/z+yuEhBvv3/P7L1ZXs/wrPdvbPyrb61YiG9tfVuPw==', 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (18.091, -13.910, -9.136), 2: (-7.239, -75.776, -0.464)}, 'hands': (0, 17), 'ik_set': {'cf_J_ArmLow01_L': ((-0.135, 1.099, -0.119), ), 'cf_J_ArmLow01_R': ((0.141, 1.098, 0.022), ), 'cf_J_ArmUp00_L': ((-0.105, 1.339, -0.085), ), 'cf_J_ArmUp00_R': ((0.099, 1.354, 0.019), ), 'cf_J_Foot01_L': ((-0.099, 0.133, -0.096), (30.419, 5.933, 358.343)), 'cf_J_Foot01_R': ((0.027, 0.079, -0.047), (0.051, 357.913, 3.545)), 'cf_J_Hand_L': ((-0.176, 0.894, -0.101), (359.247, 317.628, 51.316)), 'cf_J_Hand_R': ((0.150, 0.893, 0.066), (8.210, 353.832, 311.761)), 'cf_J_Hips': ((-0.016, 1.032, 0.003), ), 'cf_J_LegLow01_L': ((-0.053, 0.520, 0.089), ), 'cf_J_LegLow01_R': ((0.051, 0.503, 0.025), ), 'cf_J_LegUp00_L': ((-0.074, 0.880, -0.050), ), 'cf_J_LegUp00_R': ((0.076, 0.889, 0.010), )}, 'kinematic': 3, 'look_at_ptn': 3, 'move_to': (-8.341, 7.034, 12.894), 'rotate_to': (0.000, 239.474, 0.000)},
            'Me': {'anim': (1, 3, 21), 'anim_spd': 0.662, 'eyes': 1, 'face_red': 0.676, 'face_to_full2': 'BAAAAAIAAAABAACx0HvXugEAgLDq/38/MlpUPR6jvD2hW527JJB+Pw==', 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (10.726, -6.568, -9.974), 2: (-19.080, 22.070, -7.006)}, 'kinematic': 2, 'look_at_ptn': 3, 'move_to': (-7.153, 7.058, 12.781), 'rotate_to': (0.000, 259.783, 0.000)},
            'cam': {'goto_pos': ((-6.911, 8.059, 12.513), (0.000, 0.000, -2.917), (4.750, -71.300, 0.000))},
        }],
        #-VNFA:seq:end:2-#
    ], toSc2_0)

	
def toSc2_0(game):
    load_and_init_scene(game, "pool2.png", init_scene2)
	

def init_scene2(game):
    try:
        # show our game window
        game.visible = 1
        game.isHideGameButtons = 0
        
        # load actor/prop/string from scene by "tag folder", must be called after scene is loaded
        register_actor_prop_by_tag(game)
        register_string_resource(game)
        
        # import clips, after actor/prop registered
        for clip in keyframeClips:
            kfa_import(game, clip)

        # init script helper, must be called after actor/prop registered
        sh = init_script_helper(game)
        sh.createLocalizeStringOnBuild = False
        sh.masterMode = False
        sh.baseNest = "        " # base nest space of dumpped script
        sh.nestWord = "    " # space inserted when script is nested
        sh.load_python() # load this python file for auto script
        sh.asEnable = True # enable auto script feature
        
        # setup default next button
        game.btnNextText = "Next >>"

        # here game start
        toSeq3(game)

    except Exception as e:
        import traceback
        traceback.print_exc()
        toEnd(game, "init_scene FAILED: "+str(e))	
	
	

def toSeq3(game):
    game.texts_next([
        #-VNFA:seq:start:3-#
        ["Me", "Wow", act, {
            'Nia': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (5, 80, 0), 'anim_lp': 0, 'anim_ptn': 0.132, 'anim_spd': 0.706, 'cloth_all': (0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 2), 'cloth_type': 2, 'eyes': 1, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.705, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAADycPM8a4XhONr2fDoI438/8HM7vAAAAAAAAAAAtvt/Pw==', 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (19.806, 0.000, 0.000), 2: (15.252, 0.000, 0.000)}, 'hands': (7, 7), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {'cf_J_ArmLow01_L': ((-0.252, 0.629, -0.115), ), 'cf_J_ArmLow01_R': ((0.199, 0.354, -0.087), ), 'cf_J_ArmUp00_L': ((-0.124, 0.644, 0.103), ), 'cf_J_ArmUp00_R': ((0.095, 0.624, 0.090), ), 'cf_J_Foot01_L': ((-0.254, 0.117, -0.255), (66.871, 220.208, 228.461)), 'cf_J_Foot01_R': ((0.254, 0.117, -0.255), (66.871, 139.791, 131.538)), 'cf_J_Hand_L': ((-0.161, 0.259, 0.154), (342.214, 22.286, 84.753)), 'cf_J_Hand_R': ((0.181, 0.250, 0.151), (323.276, 336.607, 282.903)), 'cf_J_Hips': ((0.003, 0.420, 0.077), ), 'cf_J_LegLow01_L': ((-0.349, 0.042, 0.159), ), 'cf_J_LegLow01_R': ((0.349, 0.042, 0.159), ), 'cf_J_LegUp00_L': ((-0.081, 0.296, 0.042), ), 'cf_J_LegUp00_R': ((0.081, 0.296, 0.042), )}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 3, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 1, 'mouth_open': 0.000, 'move_to': (-13.581, 7.385, 6.358), 'nip_stand': 0.000, 'rotate_to': (0.000, 203.723, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.162, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'sys': {'bg_png': 'sample01.png', 'bgm': (0, 0), 'env': (0, 0), 'map': -1, 'map_pos': (0.000, 0.000, 0.000), 'map_rot': (0.000, 0.000, 0.000), 'wav': ('', 0, 1)},
            'Me': {'acc_all': (0, 0, 0, 0, 0, 1, 1, 1, 1, 1), 'anim': (1, 5, 0), 'anim_lp': 0, 'anim_ptn': 0.132, 'anim_spd': 0.662, 'cloth_all': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2), 'cloth_type': 2, 'eyes': 1, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.676, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAAABAACx0HvXugEAgLDq/38/MlpUPR6jvD2hW527JJB+Pw==', 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (6.245, -12.579, 3.949), 2: (14.440, 11.310, 0.000)}, 'hands': (0, 11), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 2, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 0, 'mouth_open': 0.000, 'move_to': (-13.642, 7.447, 6.313), 'nip_stand': 0.000, 'rotate_to': (0.000, 21.418, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.103, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'cam': {'goto_pos': ((-13.847, 7.463, 5.266), (0.000, 0.000, -0.073), (-27.150, 14.350, -65.596))},
        }],
        ["Nia", "Teehee, you're sweet.", act, {
            'cam': {'goto_pos': ((-13.847, 7.463, 5.266), (0.000, 0.000, -0.073), (-27.150, 14.350, -65.596))},
        }],
        ["s", "She undressed her skirt.", act, {
            'Nia': {'anim': (1, 3, 21), 'fk_set': {1: (9.781, 0.000, 0.000), 2: (15.252, 0.000, 0.000)}, 'hands': (10, 10), 'ik_set': {'cf_J_ArmLow01_L': ((-0.242, 1.103, -0.201), ), 'cf_J_ArmLow01_R': ((0.188, 1.116, -0.241), ), 'cf_J_ArmUp00_L': ((-0.158, 1.332, -0.179), ), 'cf_J_ArmUp00_R': ((0.078, 1.286, -0.092), ), 'cf_J_Foot01_L': ((-0.072, 0.077, -0.209), (359.643, 4.123, 0.635)), 'cf_J_Foot01_R': ((0.046, 0.077, -0.237), (359.756, 7.041, 359.475)), 'cf_J_Hand_L': ((-0.200, 0.925, -0.101), (301.606, 126.873, 15.248)), 'cf_J_Hand_R': ((-0.005, 0.930, -0.080), (294.939, 244.006, 336.761)), 'cf_J_Hips': ((-0.033, 1.037, -0.149), ), 'cf_J_LegLow01_L': ((-0.087, 0.504, -0.150), ), 'cf_J_LegLow01_R': ((0.048, 0.504, -0.175), ), 'cf_J_LegUp00_L': ((-0.115, 0.889, -0.174), ), 'cf_J_LegUp00_R': ((0.047, 0.891, -0.184), )}, 'move_to': (-12.896, 7.035, 5.811), 'rotate_to': (0.000, 287.072, 0.000)},
            'Me': {'anim': (1, 4, 0), 'fk_set': {1: (-18.937, -14.358, 4.150), 2: (-37.340, 11.310, -4.803)}, 'move_to': (-13.344, 7.078, 6.111), 'rotate_to': (0.000, 122.079, 0.000)},
            'cam': {'goto_pos': ((-13.932, 7.942, 7.484), (0.000, 0.000, -0.533), (-5.500, 146.600, 0.000))},
        }],
        ["s", "...", act, {
            'Nia': {'anim': (0, 0, 0), 'cloth_all': (0, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 2), 'fk_set': {1: (15.000, 12.665, 2.144), 2: (15.252, 0.000, 0.000)}, 'ik_set': {}, 'kinematic': 2},
            'cam': {'goto_pos': ((-11.548, 8.165, 8.162), (0.000, 0.000, -0.055), (1.100, 214.850, 0.000))},
        }],
        ["s", "...", act, {
            'cam': {'goto_pos': ((-14.335, 7.356, 7.840), (0.000, 0.000, -0.013), (-19.550, 145.050, 0.000))},
        }],
        ["s", "Then she undressed her bikini shorts.", act, {
            'Nia': {'anim': (5, 95, 0), 'fk_set': {1: (31.864, -12.419, 6.792), 2: (22.957, -58.201, 0.000)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.465, 1.085, 0.773), ), 'cf_J_ArmLow01_R': ((-0.789, 1.243, 0.376), ), 'cf_J_ArmUp00_L': ((-0.389, 1.060, 0.095), ), 'cf_J_ArmUp00_R': ((-0.490, 1.012, 0.002), ), 'cf_J_Foot01_L': ((-0.285, 0.071, 0.190), (0.905, 184.410, 359.961)), 'cf_J_Foot01_R': ((-0.507, 0.076, 0.415), (10.088, 195.958, 7.816)), 'cf_J_Hand_L': ((-0.248, 0.950, 0.339), (1.619, 193.723, 85.716)), 'cf_J_Hand_R': ((-0.568, 0.960, 0.228), (6.272, 172.757, 283.868)), 'cf_J_Hips': ((-0.397, 0.974, 0.118), ), 'cf_J_LegLow01_L': ((-0.182, 0.336, 0.046), ), 'cf_J_LegLow01_R': ((-0.434, 0.281, 0.159), ), 'cf_J_LegUp00_L': ((-0.354, 0.809, 0.362), ), 'cf_J_LegUp00_R': ((-0.508, 0.806, 0.322), )}, 'kinematic': 3, 'move_to': (-12.426, 7.035, 5.785), 'rotate_to': (0.000, 318.641, 0.000)},
            'Me': {'fk_set': {1: (-18.937, -14.358, 4.150), 2: (-6.589, 8.834, -3.842)}},
            'cam': {'goto_pos': ((-13.077, 7.990, 8.670), (0.000, 0.000, -0.160), (3.600, 179.500, 0.000))},
        }],
        #-VNFA:seq:end:3-#
    ], toSeq4)
	
def toSeq4(game):
    game.texts_next([
        #-VNFA:seq:start:1-#
        ["s", "...", act, {
            'Nia': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (5, 67, 0), 'anim_lp': 0, 'anim_ptn': 0.132, 'anim_spd': 0.706, 'cloth_all': (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2), 'cloth_type': 2, 'eyes': 1, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.705, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAADycPM8a4XhONr2fDoI438/8HM7vAAAAAAAAAAAtvt/Pw==', 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (28.974, 4.529, 15.422), 2: (-7.112, -43.214, 2.036)}, 'hands': (10, 10), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {'cf_J_ArmLow01_L': ((-0.465, 1.085, 0.773), ), 'cf_J_ArmLow01_R': ((-0.789, 1.243, 0.376), ), 'cf_J_ArmUp00_L': ((-0.374, 0.986, 0.109), ), 'cf_J_ArmUp00_R': ((-0.542, 0.926, 0.074), ), 'cf_J_Foot01_L': ((-0.285, 0.071, 0.190), (0.905, 184.410, 359.961)), 'cf_J_Foot01_R': ((-0.446, 0.073, 0.212), (10.088, 195.958, 7.816)), 'cf_J_Hand_L': ((-0.239, 0.724, 0.234), (1.619, 193.723, 85.716)), 'cf_J_Hand_R': ((-0.603, 0.749, 0.271), (6.272, 172.757, 283.868)), 'cf_J_Hips': ((-0.397, 0.974, 0.118), ), 'cf_J_LegLow01_L': ((-0.306, 0.340, 0.036), ), 'cf_J_LegLow01_R': ((-0.461, 0.281, -0.157), ), 'cf_J_LegUp00_L': ((-0.354, 0.809, 0.362), ), 'cf_J_LegUp00_R': ((-0.508, 0.806, 0.322), )}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 3, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 1, 'mouth_open': 0.000, 'move_to': (-12.525, 7.035, 5.785), 'nip_stand': 0.000, 'rotate_to': (0.000, 318.641, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.162, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'ninv': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (1, 3, 21), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.000, 'cloth_all': (2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 2), 'cloth_type': 2, 'eyes': 0, 'eyes_blink': 0, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAAAAAAAAAAAAAAAAAAAAAIA/AAAAAAAAAAAAAAAAAACAPw==', 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (28.974, 4.529, 15.422), 2: (-7.112, -43.214, 2.036)}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {'cf_J_ArmLow01_L': ((-0.465, 1.085, 0.773), ), 'cf_J_ArmLow01_R': ((-0.789, 1.243, 0.376), ), 'cf_J_ArmUp00_L': ((-0.374, 0.986, 0.109), ), 'cf_J_ArmUp00_R': ((-0.542, 0.926, 0.074), ), 'cf_J_Foot01_L': ((-0.285, 0.071, 0.190), (0.905, 184.410, 359.961)), 'cf_J_Foot01_R': ((-0.446, 0.073, 0.212), (10.088, 195.958, 7.816)), 'cf_J_Hand_L': ((-0.239, 0.724, 0.234), (1.619, 193.723, 85.716)), 'cf_J_Hand_R': ((-0.603, 0.749, 0.271), (6.272, 172.757, 283.868)), 'cf_J_Hips': ((-0.397, 0.974, 0.118), ), 'cf_J_LegLow01_L': ((-0.306, 0.340, 0.036), ), 'cf_J_LegLow01_R': ((-0.461, 0.281, -0.157), ), 'cf_J_LegUp00_L': ((-0.354, 0.809, 0.362), ), 'cf_J_LegUp00_R': ((-0.508, 0.806, 0.322), )}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 3, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 0, 'mouth_open': 0.000, 'move_to': (-11.859, 7.520, 5.112), 'nip_stand': 0.000, 'rotate_to': (65.636, 318.641, 0.000), 'scale_to': (1.140, 1.360, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'Me': {'acc_all': (0, 0, 0, 0, 0, 1, 1, 1, 1, 1), 'anim': (1, 4, 0), 'anim_lp': 0, 'anim_ptn': 0.132, 'anim_spd': 0.662, 'cloth_all': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2), 'cloth_type': 2, 'eyes': 1, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.676, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAAABAACx0HvXugEAgLDq/38/MlpUPR6jvD2hW527JJB+Pw==', 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (-1.642, -13.122, 3.927), 2: (-6.589, 8.834, -3.842)}, 'hands': (0, 11), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 2, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 0, 'mouth_open': 0.000, 'move_to': (-13.344, 7.078, 6.111), 'nip_stand': 0.000, 'rotate_to': (0.000, 122.079, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.103, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'sys': {'bg_png': 'sample01.png', 'bgm': (0, 0), 'env': (0, 0), 'map': -1, 'map_pos': (0.000, 0.000, 0.000), 'map_rot': (0.000, 0.000, 0.000), 'wav': ('', 0, 1)},
            'cam': {'goto_pos': ((-13.236, 7.932, 7.953), (0.000, 0.000, -0.100), (4.100, 175.900, 0.000))},
        }],
        ["s", "...", act, {
            'Nia': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (5, 67, 0), 'anim_lp': 0, 'anim_ptn': 0.132, 'anim_spd': 0.706, 'cloth_all': (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2), 'cloth_type': 2, 'eyes': 1, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.705, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAADycPM8a4XhONr2fDoI438/8HM7vAAAAAAAAAAAtvt/Pw==', 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (12.838, 43.913, 30.121), 2: (-7.112, -43.214, 2.036)}, 'hands': (10, 10), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {'cf_J_ArmLow01_L': ((-0.465, 1.085, 0.773), ), 'cf_J_ArmLow01_R': ((-0.789, 1.243, 0.376), ), 'cf_J_ArmUp00_L': ((-0.275, 0.755, -0.080), ), 'cf_J_ArmUp00_R': ((-0.472, 0.762, -0.079), ), 'cf_J_Foot01_L': ((-0.275, 0.071, 0.149), (0.905, 184.410, 359.961)), 'cf_J_Foot01_R': ((-0.457, 0.057, 0.103), (10.088, 195.958, 7.816)), 'cf_J_Hand_L': ((-0.224, 0.274, 0.223), (1.619, 193.723, 85.716)), 'cf_J_Hand_R': ((-0.556, 0.166, 0.200), (6.272, 172.757, 283.868)), 'cf_J_Hips': ((-0.343, 0.852, 0.030), ), 'cf_J_LegLow01_L': ((-0.284, 0.340, -0.120), ), 'cf_J_LegLow01_R': ((-0.461, 0.281, -0.157), ), 'cf_J_LegUp00_L': ((-0.395, 0.891, 0.341), ), 'cf_J_LegUp00_R': ((-0.549, 0.889, 0.315), )}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 3, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 1, 'mouth_open': 0.000, 'move_to': (-12.525, 7.035, 5.785), 'nip_stand': 0.000, 'rotate_to': (0.000, 318.641, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.162, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'ninv': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (1, 3, 21), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 0.000, 'cloth_all': (2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 2), 'cloth_type': 2, 'eyes': 0, 'eyes_blink': 0, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAAAAAAAAAAAAAAAAAAAAAIA/AAAAAAAAAAAAAAAAAACAPw==', 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (28.974, 4.529, 15.422), 2: (-7.112, -43.214, 2.036)}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 2, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 0, 'mouth_open': 0.000, 'move_to': (-12.786, 6.912, 5.515), 'nip_stand': 0.000, 'rotate_to': (0.000, 121.696, 0.000), 'scale_to': (1.140, 0.443, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'Me': {'acc_all': (0, 0, 0, 0, 0, 1, 1, 1, 1, 1), 'anim': (1, 4, 0), 'anim_lp': 0, 'anim_ptn': 0.132, 'anim_spd': 0.662, 'cloth_all': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2), 'cloth_type': 2, 'eyes': 1, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.676, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAAABAACx0HvXugEAgLDq/38/MlpUPR6jvD2hW527JJB+Pw==', 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (-1.642, -13.122, 3.927), 2: (-6.589, 8.834, -3.842)}, 'hands': (0, 11), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 2, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 0, 'mouth_open': 0.000, 'move_to': (-13.344, 7.078, 6.111), 'nip_stand': 0.000, 'rotate_to': (0.000, 122.079, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.103, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'sys': {'bg_png': 'sample01.png', 'bgm': (0, 0), 'env': (0, 0), 'map': -1, 'map_pos': (0.000, 0.000, 0.000), 'map_rot': (0.000, 0.000, 0.000), 'wav': ('', 0, 1)},
            'cam': {'goto_pos': ((-12.967, 7.978, 8.221), (0.000, 0.000, -0.055), (5.850, 179.850, 0.000))},
        }],
        ["Nia", "Well, what do you think? Still pretty?", act, {
            'Nia': {'anim': (2, 9, 1), 'fk_set': {1: (28.257, 3.830, 11.594), 2: (0.000, 0.000, 0.000)}, 'hands': (0, 0), 'ik_set': {}, 'kinematic': 2, 'move_to': (-12.793, 7.035, 5.536)},
            'ninv': {'visible': 0},
            'Me': {'fk_set': {1: (-22.217, -14.615, 4.240), 2: (-6.589, 8.834, -3.842)}},
            'cam': {'goto_pos': ((-13.581, 7.694, 7.017), (0.000, 0.000, -0.505), (-16.250, 156.350, 0.000))},
        }],
        ["Me", "Yes! You are beautiful.", act, {
            'cam': {'goto_pos': ((-11.570, 7.856, 8.617), (0.000, 0.000, -0.097), (-2.650, 205.900, 0.000))},
        }],
        ["Nia", "Good answer. Now get up.", act, {
            'cam': {'goto_pos': ((-11.570, 7.856, 8.617), (0.000, 0.000, -0.097), (-2.650, 205.900, 0.000))},
        }],
        ["s", "...", act, {
            'Me': {'anim': (1, 3, 21), 'move_to': (-12.891, 7.046, 5.817), 'rotate_to': (0.000, 102.117, 0.000)},
            'cam': {'goto_pos': ((-12.924, 7.905, 8.156), (0.000, 0.000, -0.010), (-5.100, 177.050, 0.000))},
        }],
        #-VNFA:seq:end:1-#
    ], toSc2_0)
	
#-VNFA:sel:empty:1-#

#########################################################################################################################################	
#########################################################################################################################################	
#########################################################################################################################################	
	
	
def toSc2_0(game):
    load_and_init_scene(game, "pool2.png", init_scene2)

def init_scene2(game):
    try:
        # show our game window
        game.visible = 1
        game.isHideGameButtons = 0
        
        # load actor/prop/string from scene by "tag folder", must be called after scene is loaded
        register_actor_prop_by_tag(game)
        register_string_resource(game)
        
        # import clips, after actor/prop registered
        for clip in keyframeClips:
            kfa_import(game, clip)

        # init script helper, must be called after actor/prop registered
        sh = init_script_helper(game)
        sh.createLocalizeStringOnBuild = False
        sh.masterMode = False
        sh.baseNest = "        " # base nest space of dumpped script
        sh.nestWord = "    " # space inserted when script is nested
        sh.load_python() # load this python file for auto script
        sh.asEnable = True # enable auto script feature
        
        # setup default next button
        game.btnNextText = "Next >>"

        # here game start
        toSc5_0(game)

    except Exception as e:
        import traceback
        traceback.print_exc()
        toEnd(game, "init_scene FAILED: "+str(e))	
		
		
def toSeq2(game):
    game.texts_next([
        #-VNFA:seq:empty:2-#
    ], toSc5_0)


#########################################################################################################################################	
#########################################################################################################################################	
#########################################################################################################################################	
	
	
def toSc5_0(game):
    load_and_init_scene(game, "pool5.png", init_scene5)

def init_scene5(game):
    try:
        # show our game window
        game.visible = 1
        game.isHideGameButtons = 0
        
        # load actor/prop/string from scene by "tag folder", must be called after scene is loaded
        register_actor_prop_by_tag(game)
        register_string_resource(game)
        
        # import clips, after actor/prop registered
        for clip in keyframeClips:
            kfa_import(game, clip)

        # init script helper, must be called after actor/prop registered
        sh = init_script_helper(game)
        sh.createLocalizeStringOnBuild = False
        sh.masterMode = False
        sh.baseNest = "        " # base nest space of dumpped script
        sh.nestWord = "    " # space inserted when script is nested
        sh.load_python() # load this python file for auto script
        sh.asEnable = True # enable auto script feature
        
        # setup default next button
        game.btnNextText = "Next >>"

        # here game start
        toSeq5(game)

    except Exception as e:
        import traceback
        traceback.print_exc()
        toEnd(game, "init_scene FAILED: "+str(e))		

def toSeq5(game):
    game.texts_next([
        #-VNFA:seq:empty:1-#
    ], toSc6_0)

#########################################################################################################################################	
#########################################################################################################################################	
#########################################################################################################################################	
	
	
def toSc6_0(game):
    load_and_init_scene(game, "pool6.png", init_scene6)

def init_scene6(game):
    try:
        # show our game window
        game.visible = 1
        game.isHideGameButtons = 0
        
        # load actor/prop/string from scene by "tag folder", must be called after scene is loaded
        register_actor_prop_by_tag(game)
        register_string_resource(game)
        
        # import clips, after actor/prop registered
        for clip in keyframeClips:
            kfa_import(game, clip)

        # init script helper, must be called after actor/prop registered
        sh = init_script_helper(game)
        sh.createLocalizeStringOnBuild = False
        sh.masterMode = False
        sh.baseNest = "        " # base nest space of dumpped script
        sh.nestWord = "    " # space inserted when script is nested
        sh.load_python() # load this python file for auto script
        sh.asEnable = True # enable auto script feature
        
        # setup default next button
        game.btnNextText = "Next >>"

        # here game start
        toSeq6(game)

    except Exception as e:
        import traceback
        traceback.print_exc()
        toEnd(game, "init_scene FAILED: "+str(e))	

		
		
def toSeq6(game):
    game.texts_next([
        #-VNFA:seq:start:1-#
        ["Me", "Ahhh...", act, {
            'Nia': {'acc_all': (0, 1, 0, 0, 0, 0, 0, 0, 0, 0), 'anim': (5, 80, 0), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.081, 'cloth_all': (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2), 'cloth_type': 1, 'eyes': 1, 'eyes_blink': 0, 'eyes_open': 0.853, 'face_red': 0.000, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAABxml0+/v8DMP7/n7D57nk/w4xdPp2arzzvspu7jd95Pw==', 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (18.230, -52.173, -21.944), 2: (7.022, 2.960, 18.301)}, 'hands': (1, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {'cf_J_ArmLow01_L': ((-0.207, 0.272, 0.348), ), 'cf_J_ArmLow01_R': ((0.151, 0.399, 0.567), ), 'cf_J_ArmUp00_L': ((-0.129, 0.454, 0.265), ), 'cf_J_ArmUp00_R': ((0.112, 0.509, 0.439), ), 'cf_J_Foot01_L': ((-0.272, 0.134, -0.556), (67.007, 220.812, 228.954)), 'cf_J_Foot01_R': ((0.206, 0.111, -0.097), (67.006, 139.187, 131.046)), 'cf_J_Hand_L': ((-0.065, 0.266, -0.006), (288.633, 346.916, 220.487)), 'cf_J_Hand_R': ((0.081, 0.211, 0.809), (344.733, 266.130, 3.128)), 'cf_J_Hips': ((0.005, 0.479, 0.235), ), 'cf_J_LegLow01_L': ((-0.297, 0.047, 0.182), ), 'cf_J_LegLow01_R': ((0.175, 0.104, 0.494), ), 'cf_J_LegUp00_L': ((-0.131, 0.413, 0.027), ), 'cf_J_LegUp00_R': ((0.119, 0.397, 0.043), )}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 3, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 2, 'mouth_open': 0.368, 'move_to': (-23.932, 7.377, 30.447), 'nip_stand': 0.000, 'rotate_to': (0.000, 359.409, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'sys': {'bg_png': '', 'bgm': (0, 0), 'env': (0, 0), 'map': -1, 'map_pos': (0.000, 0.000, 0.000), 'map_rot': (0.000, 0.000, 0.000), 'wav': ('', 0, 1)},
            'Me': {'acc_all': (0, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (3, 32, 1), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 0.265, 'cloth_all': (0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 2), 'cloth_type': 0, 'eyes': 1, 'eyes_blink': 0, 'eyes_open': 1.000, 'face_red': 0.176, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAAAAAAAAAAAAAAAAAAAAAIA/W23MvB50Irw9xYG5X+h/Pw==', 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (40.399, 30.774, 3.315), 2: (-5.523, -12.891, 4.942)}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {'cf_J_ArmLow01_L': ((-0.248, -0.109, -0.225), ), 'cf_J_ArmLow01_R': ((0.172, 0.030, -0.197), ), 'cf_J_ArmUp00_L': ((-0.106, 0.055, -0.397), ), 'cf_J_ArmUp00_R': ((0.099, 0.058, -0.401), ), 'cf_J_Foot01_L': ((-0.174, -0.021, 0.745), (290.416, 15.596, 348.820)), 'cf_J_Foot01_R': ((0.205, 0.001, 0.636), (358.051, 357.081, 5.060)), 'cf_J_Hand_L': ((-0.151, 0.064, 0.019), (326.511, 80.052, 7.758)), 'cf_J_Hand_R': ((0.150, 0.035, 0.006), (319.875, 294.876, 350.554)), 'cf_J_Hips': ((-0.027, 0.024, -0.123), ), 'cf_J_LegLow01_L': ((-0.146, 0.327, 0.306), ), 'cf_J_LegLow01_R': ((0.140, 0.330, 0.300), ), 'cf_J_LegUp00_L': ((-0.070, 0.078, 0.006), ), 'cf_J_LegUp00_R': ((0.059, 0.100, 0.029), )}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 3, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 12, 'mouth_open': 0.000, 'move_to': (-23.958, 7.511, 30.459), 'nip_stand': 0.000, 'rotate_to': (1.699, 180.842, 359.278), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'cam': {'goto_pos': ((-22.438, 7.445, 33.548), (0.000, 0.000, -3.892), (4.470, 31.140, -0.411))},
        }],
        ["Nia", "See it goes in there...", act, {
            'Nia': {'acc_all': (0, 1, 0, 0, 0, 0, 0, 0, 0, 0), 'anim': (5, 80, 0), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.081, 'cloth_all': (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2), 'cloth_type': 1, 'eyes': 1, 'eyes_blink': 0, 'eyes_open': 0.853, 'face_red': 0.000, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAABxml0+/v8DMP7/n7D57nk/w4xdPp2arzzvspu7jd95Pw==', 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (18.230, -52.173, -21.944), 2: (7.022, 2.960, 18.301)}, 'hands': (1, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {'cf_J_ArmLow01_L': ((-0.207, 0.272, 0.348), ), 'cf_J_ArmLow01_R': ((0.151, 0.399, 0.567), ), 'cf_J_ArmUp00_L': ((-0.129, 0.454, 0.265), ), 'cf_J_ArmUp00_R': ((0.112, 0.509, 0.439), ), 'cf_J_Foot01_L': ((-0.272, 0.134, -0.556), (67.007, 220.812, 228.954)), 'cf_J_Foot01_R': ((0.206, 0.111, -0.097), (67.006, 139.187, 131.046)), 'cf_J_Hand_L': ((-0.065, 0.266, -0.006), (288.633, 346.916, 220.487)), 'cf_J_Hand_R': ((0.081, 0.211, 0.809), (344.733, 266.130, 3.128)), 'cf_J_Hips': ((0.005, 0.479, 0.235), ), 'cf_J_LegLow01_L': ((-0.297, 0.047, 0.182), ), 'cf_J_LegLow01_R': ((0.175, 0.104, 0.494), ), 'cf_J_LegUp00_L': ((-0.131, 0.413, 0.027), ), 'cf_J_LegUp00_R': ((0.119, 0.397, 0.043), )}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 3, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 2, 'mouth_open': 0.368, 'move_to': (-23.932, 7.377, 30.447), 'nip_stand': 0.000, 'rotate_to': (0.000, 359.409, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'sys': {'bg_png': '', 'bgm': (0, 0), 'env': (0, 0), 'map': -1, 'map_pos': (0.000, 0.000, 0.000), 'map_rot': (0.000, 0.000, 0.000), 'wav': ('', 0, 1)},
            'Me': {'acc_all': (0, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (3, 32, 1), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 0.265, 'cloth_all': (0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 2), 'cloth_type': 0, 'eyes': 1, 'eyes_blink': 0, 'eyes_open': 1.000, 'face_red': 0.176, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAAAAAAAAAAAAAAAAAAAAAIA/W23MvB50Irw9xYG5X+h/Pw==', 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (40.399, 30.774, 3.315), 2: (-5.523, -12.891, 4.942)}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {'cf_J_ArmLow01_L': ((-0.248, -0.109, -0.225), ), 'cf_J_ArmLow01_R': ((0.172, 0.030, -0.197), ), 'cf_J_ArmUp00_L': ((-0.106, 0.055, -0.397), ), 'cf_J_ArmUp00_R': ((0.099, 0.058, -0.401), ), 'cf_J_Foot01_L': ((-0.174, -0.021, 0.745), (290.416, 15.596, 348.820)), 'cf_J_Foot01_R': ((0.205, 0.001, 0.636), (358.051, 357.081, 5.060)), 'cf_J_Hand_L': ((-0.151, 0.064, 0.019), (326.511, 80.052, 7.758)), 'cf_J_Hand_R': ((0.150, 0.035, 0.006), (319.875, 294.876, 350.554)), 'cf_J_Hips': ((-0.027, 0.024, -0.123), ), 'cf_J_LegLow01_L': ((-0.146, 0.327, 0.306), ), 'cf_J_LegLow01_R': ((0.140, 0.330, 0.300), ), 'cf_J_LegUp00_L': ((-0.070, 0.078, 0.006), ), 'cf_J_LegUp00_R': ((0.059, 0.100, 0.029), )}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 3, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 12, 'mouth_open': 0.000, 'move_to': (-23.958, 7.511, 30.459), 'nip_stand': 0.000, 'rotate_to': (1.699, 180.842, 359.278), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'cam': {'goto_pos': ((-22.438, 7.445, 33.548), (0.000, 0.000, -3.892), (4.470, 31.140, -0.411))},
        }],
        #-VNFA:seq:end:1-#
    ], toEnd)
		
    
def toEnd(game, text = None):
    if text == None:
        text = "<size=32>THE END</size>"
    game.set_text_s(text)
    if True:
        game.set_buttons(["Restart <<", "End Game >>"], [start, clearExit])
    else:
        clearExit(game)

def clearExit(game):
    clear_keyframe_anime(game)
    game.scenePNG = ""
    game.return_to_start_screen_clear()

# Keyframe clips build by clip manager
keyframeClips = [
#-VNFA:KeyFrameClips:start-#
#-VNFA:KeyFrameClips:end-#
]
