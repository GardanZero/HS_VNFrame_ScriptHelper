#vngame;neo;fun2
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
    game.sceneDir = "fun1\\"
    if enableQuickReload and hasattr(game, "scenePNG") and game.scenePNG == "fun2.png":
        # skip load png, quick reload
        # all actor/prop status must be reset by script
        init_scene(game)
    else:
        load_and_init_scene(game, "fun2.png", init_scene)
    
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
        menuSkip(game)

    except Exception as e:
        import traceback
        traceback.print_exc()
        toEnd(game, "init_scene FAILED: "+str(e))

def menuSkip(game):    
	game.set_text("Boy", "What should I do?")
	game.set_buttons(["Go to Seq7", "Go To End"], [toSeq7, toEnd])

def toSeq3(game):
    game.texts_next([
        #-VNFA:seq:start:3-#
        ["SMing", "Ah, Thomas, good that you are here. Did your mom drop you off?", act, {
		'bonr': {'visible': 0},
            'SNia': {'acc_all': (1, 1, 0, 1, 1, 1, 1, 1, 1, 1), 'anim': (2, 10, 0), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.000, 'cloth_all': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 'cloth_type': 0, 'eyes': 1, 'eyes_blink': 0, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full': (4, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 63, 89, 175, 79, 61, 210, 38, 18, 61, 214, 151, 237, 186, 208, 129, 127, 63), 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 1, 'mouth_open': 0.000, 'move_to': (-6.403, 0.008, 49.921), 'nip_stand': 0.000, 'rotate_to': (0.000, 330.187, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'cam': {'goto_pos': ((-6.563, 2.692, 49.831), (0.000, 0.000, -0.193), (29.300, 332.798, 0.000))},
            'STans': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (2, 13, 0), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.081, 'cloth_all': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 'cloth_type': 1, 'eyes': 1, 'eyes_blink': 0, 'eyes_open': 1.000, 'face_red': 0.243, 'face_to': 4, 'face_to_full': (4, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 63, 246, 112, 187, 61, 147, 185, 33, 188, 178, 216, 109, 58, 181, 233, 126, 63), 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (24.311, 8.155, -18.960), 2: (15.021, -6.516, 6.730)}, 'hands': (8, 1), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 2, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 1, 'mouth_open': 0.588, 'move_to': (-4.920, 0.006, 50.259), 'nip_stand': 0.000, 'rotate_to': (0.000, 315.117, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.191, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'SLim': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (1, 4, 4), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.000, 'cloth_all': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 'cloth_type': 0, 'eyes': 0, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full': (4, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 63, 120, 97, 69, 189, 149, 227, 120, 190, 58, 23, 70, 188, 74, 255, 119, 63), 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 1, 'mouth_open': 0.235, 'move_to': (-5.721, -0.020, 49.907), 'nip_stand': 0.000, 'rotate_to': (0.000, 342.696, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'SJean': {'acc_all': (0, 1, 0, 1, 0, 0, 0, 0, 0, 0), 'anim': (1, 4, 0), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 0.427, 'cloth_all': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 'cloth_type': 1, 'eyes': 0, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full': (4, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 63, 193, 49, 242, 189, 14, 23, 36, 190, 11, 114, 158, 188, 167, 210, 122, 63), 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 1, 'mouth_open': 0.000, 'move_to': (-4.372, 0.002, 50.763), 'nip_stand': 0.000, 'rotate_to': (0.000, 316.548, 0.000), 'scale_to': (0.900, 0.900, 0.900), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'SBoy': {'acc_all': (0, 1, 1, 1, 1, 1, 0, 1, 0, 1), 'anim': (1, 3, 21), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 0.926, 'cloth_all': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 'cloth_type': 0, 'eyes': 0, 'eyes_blink': 0, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full': (4, 0, 0, 0, 2, 0, 0, 0, 121, 206, 169, 188, 252, 255, 127, 174, 253, 255, 191, 49, 235, 241, 127, 63, 13, 129, 58, 190, 112, 246, 155, 62, 143, 144, 115, 61, 137, 217, 110, 63), 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 0, 'mouth_open': 0.000, 'move_to': (-7.678, 0.031, 52.564), 'nip_stand': 0.000, 'rotate_to': (0.000, 134.294, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'sys': {'bg_png': '', 'bgm': (0, 0), 'env': (0, 0), 'map': -1, 'map_pos': (0.000, 0.000, 0.000), 'map_rot': (0.000, 0.000, 0.000), 'wav': ('', 0, 1)},
            'SMing': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (1, 3, 21), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.000, 'cloth_all': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 'cloth_type': 0, 'eyes': 0, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full': (4, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 63, 180, 9, 11, 62, 84, 88, 232, 60, 154, 216, 126, 187, 249, 133, 125, 63), 'fk_active': (0, 0, 0, 1, 0, 0, 0), 'fk_set': {}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 1, 'mouth_open': 0.000, 'move_to': (-7.653, 0.013, 51.991), 'nip_stand': 0.000, 'rotate_to': (0.000, 349.715, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
        }],
        ["SBoy", "Yes, she did, she'll pick me up in a few hours.", act, {
            'cam': {'goto_pos': ((-6.981, 0.696, 54.057), (0.000, 0.000, -0.157), (-17.000, 198.948, 0.000))},
        }],
        ["SMing", "Very good. Now, you probably don't know why your are here...", act, {
            'cam': {'goto_pos': ((-6.851, 2.400, 50.770), (0.000, 0.000, 0.000), (31.850, 330.998, 0.000))},
        }],
        ["s", "The boy listened.", act, {
            'cam': {'goto_pos': ((-6.851, 2.400, 50.770), (0.000, 0.000, 0.000), (31.850, 330.998, 0.000))},
        }],
        ["SMing", "We are all members of the feminist club.", act, {
            'cam': {'goto_pos': ((-6.981, 0.696, 54.057), (0.000, 0.000, -0.157), (-16.900, 198.948, 0.000))},
        }],
        ["s", "The boy looked at the other people in the room.", act, {
            'cam': {'goto_pos': ((-6.981, 0.696, 54.057), (0.000, 0.000, -0.157), (-16.900, 198.948, 0.000))},
        }],
        ["s", "He saw a young japanse girl, who apparently went to high school.", act, {
            'cam': {'goto_pos': ((-6.788, 1.472, 50.768), (0.000, 0.000, -0.263), (-1.300, 154.298, 0.000))},
        }],
        ["s", "A half-chinese lady, who smiled brightly at him.", act, {
            'cam': {'goto_pos': ((-6.552, 1.105, 50.981), (0.000, 0.000, -0.280), (3.650, 139.548, 0.000))},
        }],
        ["s", "An older woman, who was a school friends' mom, but he didn't recall whose.", act, {
            'cam': {'goto_pos': ((-6.073, 1.438, 51.009), (0.000, 0.000, -0.268), (1.750, 120.798, 0.000))},
        }],
        ["s", "And another high school student.", act, {
            'cam': {'goto_pos': ((-5.420, 0.983, 51.442), (0.000, 0.000, -0.313), (3.650, 121.648, 0.000))},
        }],
        ["SMing", "And our club has taken charge to educate young men like yourself in proper 'behavior' around women. You see?", act, {
            'cam': {'goto_pos': ((-7.282, 1.049, 53.710), (0.000, 0.000, -0.045), (-12.450, 191.298, 0.000))},
        }],
        ["s", "Oh, so they going to teach him manners, like at a dinner table... how boring.", act, {
            'cam': {'goto_pos': ((-6.889, 2.283, 50.793), (0.000, 0.000, 0.000), (29.650, 327.748, 0.000))},
        }],
        ["SBoy", "I think so.", act, {
            'cam': {'goto_pos': ((-6.889, 2.283, 50.793), (0.000, 0.000, 0.000), (29.600, 327.748, 0.000))},
        }],
        ["SMing", "So all of us are going to be your teachers. That's why your mom brought you here.", act, {
            'cam': {'goto_pos': ((-8.532, 1.128, 55.217), (0.000, 0.000, -0.010), (-1.350, 154.648, 0.000))},
        }],
        ["SMing", "And you have to do exactly as we say, even if it might sound very strange to you. Do you understand?", act, {
            'cam': {'goto_pos': ((-8.532, 1.128, 55.217), (0.000, 0.000, -0.010), (-1.350, 154.648, 0.000))},
        }],
        ["SBoy", "Uhh... yes, ok.", act, {
            'cam': {'goto_pos': ((-6.851, 2.400, 50.770), (0.000, 0.000, 0.000), (31.850, 330.948, 0.000))},
        }],
        ["SMing", "Great. You are now an honorary member of our club. And there is one more rule. You are not allowed to talk about anything that happens in this club. It's a big secret. Do you agree?", act, {
            'cam': {'goto_pos': ((-8.532, 1.128, 55.217), (0.000, 0.000, -0.010), (-1.300, 154.648, 0.000))},
        }],
        ["SBoy", "Sure, ok.", act, {
            'cam': {'goto_pos': ((-6.851, 2.400, 50.770), (0.000, 0.000, 0.000), (31.850, 330.948, 0.000))},
        }],
        ["SMing", "You're not taking this seriously enough. Do you really agree to do anything we say and not to talk about it to ANYONE?", act, {
            'SMing': {'eyes': 3, 'mouth': 0},
            'cam': {'goto_pos': ((-8.532, 1.128, 55.217), (0.000, 0.000, -0.010), (-1.550, 154.648, 0.000))},
        }],
        ["SBoy", "I... Yes, yes, I promise.", act, {
            'cam': {'goto_pos': ((-6.851, 2.400, 50.770), (0.000, 0.000, 0.000), (31.850, 330.948, 0.000))},
        }],
        ["SMing", "Good, come over here.", act, {
            'SMing': {'eyes': 0, 'mouth': 1},
            'cam': {'goto_pos': ((-8.127, 0.939, 53.715), (0.000, 0.000, -0.005), (-16.300, 165.848, 0.000))},
        }],
   
        #-VNFA:seq:end:3-#
    ], toSeq7)


def toSeq7(game):
    game.texts_next([
        #-VNFA:seq:start:7-#
        ["s", "seated", act, {
            'SNia': {'acc_all': (1, 1, 0, 1, 1, 1, 1, 1, 1, 1), 'anim': (1, 4, 0), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.000, 'cloth_all': (2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2), 'cloth_type': 0, 'eyes': 1, 'eyes_blink': 0, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAAAAAAAAuE/Mvfz/f7ESuX4/GPqtvZehn74TX+W8zChyPw==', 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {}, 'hands': (1, 1), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 1, 'mouth_open': 0.000, 'move_to': (-4.294, 0.008, 52.430), 'nip_stand': 0.000, 'rotate_to': (0.000, 275.957, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'cam': {'goto_pos': ((-6.596, 1.234, 54.031), (0.000, 0.000, -0.273), (6.800, -219.303, 0.000))},
            'STans': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (1, 4, 0), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.081, 'cloth_all': (2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2), 'cloth_type': 1, 'eyes': 1, 'eyes_blink': 0, 'eyes_open': 1.000, 'face_red': 0.243, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAAD+f422/v+Rsvz/f7EAAIA/lJYyvrz9mb0r21q8QFF7Pw==', 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {}, 'hands': (8, 1), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 1, 'mouth_open': 0.000, 'move_to': (-4.319, -0.023, 51.644), 'nip_stand': 0.000, 'rotate_to': (0.000, 269.142, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.191, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'bonr': {'color': (((0.31, 0.31, 0.31, 1.00), (0.80, 0.80, 0.80, 1.00), 0.000, 0.000), ), 'fk_set': ((0.000, 0.000, 0.000), ), 'move_to': (-0.005, -0.109, 0.061), 'rotate_to': (359.596, 100.713, 29.567), 'scale_to': (0.346, 1.334, 0.245), 'visible': 1},
            'SLim': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (1, 4, 0), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.000, 'cloth_all': (2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 'cloth_type': 1, 'eyes': 0, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAAAAAAAAAAAAAAAAAAAAAIA/SWL0vbadnL79ah69tZpxPw==', 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 1, 'mouth_open': 0.000, 'move_to': (-4.311, -0.020, 52.098), 'nip_stand': 0.000, 'rotate_to': (0.000, 271.405, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'SJean': {'acc_all': (0, 1, 0, 1, 0, 0, 0, 0, 0, 0), 'anim': (1, 4, 0), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 0.427, 'cloth_all': (2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2), 'cloth_type': 1, 'eyes': 0, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAAAAAAAAAAAAAAAAAAAAAIA/WqgtvubdFD7SRc88nHJ5Pw==', 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 1, 'mouth_open': 0.000, 'move_to': (-4.369, 0.016, 51.132), 'nip_stand': 0.000, 'rotate_to': (0.000, 276.224, 0.000), 'scale_to': (0.900, 0.900, 0.900), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'SBoy': {'acc_all': (0, 1, 1, 1, 1, 1, 0, 1, 0, 1), 'anim': (2, 10, 7), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 0.926, 'cloth_all': (2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2), 'cloth_type': 1, 'eyes': 2, 'eyes_blink': 0, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAABc1eo8AukGu/qtdzjv5H8/TDZ7Pb3lary3+GY62n1/Pw==', 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 2, 'mouth_open': 0.000, 'move_to': (-5.276, -0.001, 51.448), 'nip_stand': 0.000, 'rotate_to': (0.000, 94.498, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'sys': {'bg_png': '', 'bgm': (0, 0), 'env': (0, 0), 'map': -1, 'map_pos': (0.000, 0.000, 0.000), 'map_rot': (0.000, 0.000, 0.000), 'wav': ('', 0, 1)},
            'SMing': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (1, 4, 4), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 0.000, 'cloth_all': (2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 'cloth_type': 1, 'eyes': 0, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAAAAAAAAAAAAAAAAAAAAAIA/BNDZvevppj0ZUA88ga59Pw==', 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 1, 'mouth_open': 0.000, 'move_to': (-4.398, -0.006, 50.651), 'nip_stand': 0.000, 'rotate_to': (0.000, 290.280, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
        }],
        #-VNFA:seq:end:7-#
    ], toSeq8)	
	
	
def choice1(game):    
    game.set_text("Ming", "Who do you want as your first teacher?")
    game.set_buttons(["Tanselle", "Go To End"], [toSeq4, toEnd])
	
def toSeq4(game):
    game.texts_next([
        #-VNFA:seq:start:4-#
        ["s", "start Tanselle", act, {
           
 'SNia': {'acc_all': (1, 1, 0, 1, 1, 1, 1, 1, 1, 1), 'anim': (2, 14, 2), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.000, 'cloth_all': (2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2), 'cloth_type': 0, 'eyes': 1, 'eyes_blink': 0, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full': (4, 0, 0, 0, 2, 0, 0, 0, 171, 72, 156, 61, 252, 255, 45, 50, 250, 255, 127, 178, 231, 64, 127, 63, 171, 49, 69, 62, 227, 253, 151, 189, 88, 85, 111, 60, 4, 118, 122, 63), 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (0.133, 0.000, 0.000), 2: (27.914, -13.555, 0.059)}, 'hands': (1, 1), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 2, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 1, 'mouth_open': 0.000, 'move_to': (-5.309, 0.008, 52.430), 'nip_stand': 0.000, 'rotate_to': (0.000, 148.146, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'cam': {'goto_pos': ((-5.774, 1.196, 47.203), (0.000, 0.000, -1.709), (16.700, -211.553, 0.000))},
            'STans': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (5, 80, 2), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.081, 'cloth_all': (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2), 'cloth_type': 1, 'eyes': 1, 'eyes_blink': 0, 'eyes_open': 1.000, 'face_red': 0.243, 'face_to': 4, 'face_to_full': (4, 0, 0, 0, 2, 0, 0, 0, 86, 224, 248, 61, 0, 0, 0, 0, 0, 0, 0, 0, 76, 26, 126, 63, 192, 186, 39, 62, 234, 233, 2, 62, 185, 106, 175, 188, 76, 90, 122, 63), 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (24.311, 8.155, -18.960), 2: (15.021, -6.516, 6.730)}, 'hands': (8, 1), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 2, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 1, 'mouth_open': 0.434, 'move_to': (-5.000, 0.598, 46.140), 'nip_stand': 0.000, 'rotate_to': (0.000, 274.384, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.191, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'bonr': {'color': (((0.31, 0.31, 0.31, 1.00), (0.80, 0.80, 0.80, 1.00), 0.000, 0.000), ), 'fk_set': ((0.000, 0.000, 0.000), ), 'move_to': (-0.005, -0.109, 0.061), 'rotate_to': (359.596, 100.713, 29.567), 'scale_to': (0.346, 1.334, 0.245), 'visible': 0},
            'SLim': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (2, 15, 3), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.000, 'cloth_all': (2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 'cloth_type': 1, 'eyes': 0, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full': (4, 0, 0, 0, 2, 0, 0, 0, 55, 5, 131, 61, 243, 255, 62, 51, 242, 255, 77, 179, 193, 121, 127, 63, 240, 164, 53, 62, 109, 201, 34, 190, 46, 246, 237, 60, 48, 133, 120, 63), 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {1: (3.147, 0.583, -6.684), 2: (16.673, -19.201, -7.740), 9: (0.008, -0.866, 0.844), 13: (-0.021, 1.474, 0.711)}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {'cf_J_ArmLow01_L': ((-0.095, 1.117, -0.084), ), 'cf_J_ArmLow01_R': ((0.185, 1.224, 0.189), ), 'cf_J_ArmUp00_L': ((-0.104, 1.350, 0.001), ), 'cf_J_ArmUp00_R': ((0.129, 1.377, 0.001), ), 'cf_J_Foot01_L': ((-0.048, 0.080, -0.008), (359.628, 4.413, 359.288)), 'cf_J_Foot01_R': ((0.047, 0.080, -0.045), (359.232, 354.615, 359.156)), 'cf_J_Hand_L': ((-0.010, 0.932, -0.149), (345.364, 89.016, 106.666)), 'cf_J_Hand_R': ((0.135, 1.408, 0.093), (31.624, 189.406, 90.302)), 'cf_J_Hips': ((0.027, 1.052, 0.044), ), 'cf_J_LegLow01_L': ((-0.061, 0.515, 0.046), ), 'cf_J_LegLow01_R': ((0.071, 0.505, 0.061), ), 'cf_J_LegUp00_L': ((-0.070, 0.908, 0.031), ), 'cf_J_LegUp00_R': ((0.093, 0.895, 0.017), )}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 3, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 1, 'mouth_open': 0.000, 'move_to': (-5.619, -0.020, 52.118), 'nip_stand': 0.000, 'rotate_to': (0.000, 86.159, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'SJean': {'acc_all': (0, 1, 0, 1, 0, 0, 0, 0, 0, 0), 'anim': (2, 11, 1), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 0.427, 'cloth_all': (2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2), 'cloth_type': 1, 'eyes': 0, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 3, 'face_to_full': (), 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 1, 'mouth_open': 0.000, 'move_to': (-5.515, 0.002, 51.090), 'nip_stand': 0.000, 'rotate_to': (0.000, 36.828, 0.000), 'scale_to': (0.900, 0.900, 0.900), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'SBoy': {'acc_all': (0, 1, 1, 1, 1, 1, 0, 1, 1, 1), 'anim': (3, 32, 1), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 0.926, 'cloth_all': (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2), 'cloth_type': 0, 'eyes': 2, 'eyes_blink': 0, 'eyes_open': 0.044, 'face_red': 0.478, 'face_to': 4, 'face_to_full': (4, 0, 0, 0, 2, 0, 0, 0, 212, 29, 12, 189, 97, 119, 215, 59, 28, 92, 156, 60, 72, 204, 127, 63, 192, 144, 103, 61, 141, 204, 81, 60, 243, 222, 18, 188, 43, 143, 127, 63), 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (-2.101, -8.752, 6.284), 2: (-2.787, -8.840, 6.281)}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {'cf_J_ArmLow01_L': ((-0.176, 0.031, -0.191), ), 'cf_J_ArmLow01_R': ((0.172, 0.030, -0.197), ), 'cf_J_ArmUp00_L': ((-0.106, 0.055, -0.386), ), 'cf_J_ArmUp00_R': ((0.099, 0.058, -0.401), ), 'cf_J_Foot01_L': ((-0.238, -0.045, 0.531), (357.139, 5.296, 356.116)), 'cf_J_Foot01_R': ((0.196, -0.061, 0.537), (358.051, 357.081, 5.060)), 'cf_J_Hand_L': ((-0.138, 0.041, 0.002), (326.511, 80.052, 7.758)), 'cf_J_Hand_R': ((0.150, 0.035, 0.006), (319.875, 294.876, 350.554)), 'cf_J_Hips': ((-0.025, 0.042, -0.127), ), 'cf_J_LegLow01_L': ((-0.146, 0.327, 0.306), ), 'cf_J_LegLow01_R': ((0.140, 0.330, 0.300), ), 'cf_J_LegUp00_L': ((-0.079, 0.097, 0.003), ), 'cf_J_LegUp00_R': ((0.066, 0.098, 0.000), )}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 3, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 2, 'mouth_open': 0.625, 'move_to': (-5.000, 0.708, 46.129), 'nip_stand': 0.000, 'rotate_to': (0.000, 88.563, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.272, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'sys': {'bg_png': '', 'bgm': (0, 0), 'env': (0, 0), 'map': -1, 'map_pos': (0.000, 0.000, 0.000), 'map_rot': (0.000, 0.000, 0.000), 'wav': ('', 0, 1)},
            'SMing': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (2, 11, 3), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 0.000, 'cloth_all': (2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 'cloth_type': 1, 'eyes': 0, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full': (4, 0, 0, 0, 2, 0, 0, 0, 226, 29, 152, 61, 247, 127, 34, 51, 249, 255, 132, 179, 249, 74, 127, 63, 136, 103, 67, 62, 70, 11, 189, 189, 27, 173, 147, 60, 196, 35, 122, 63), 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {1: (10.621, -1.970, -3.058), 2: (9.034, -2.155, 0.720), 9: (-0.335, 0.562, -0.565), 13: (-3.074, -0.679, 0.656)}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {'cf_J_ArmLow01_L': ((-0.244, 1.124, -0.203), ), 'cf_J_ArmLow01_R': ((0.162, 1.141, -0.239), ), 'cf_J_ArmUp00_L': ((-0.160, 1.355, -0.170), ), 'cf_J_ArmUp00_R': ((0.072, 1.368, -0.195), ), 'cf_J_Foot01_L': ((-0.073, 0.078, -0.212), (359.661, 4.118, 0.624)), 'cf_J_Foot01_R': ((0.046, 0.078, -0.241), (359.757, 7.033, 359.467)), 'cf_J_Hand_L': ((-0.115, 1.110, -0.034), (300.615, 123.864, 18.677)), 'cf_J_Hand_R': ((0.065, 1.124, -0.050), (294.363, 248.143, 324.151)), 'cf_J_Hips': ((-0.033, 1.054, -0.150), ), 'cf_J_LegLow01_L': ((-0.088, 0.512, -0.153), ), 'cf_J_LegLow01_R': ((0.049, 0.512, -0.178), ), 'cf_J_LegUp00_L': ((-0.117, 0.904, -0.176), ), 'cf_J_LegUp00_R': ((0.048, 0.905, -0.188), )}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 3, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 1, 'mouth_open': 0.000, 'move_to': (-5.668, 0.013, 51.583), 'nip_stand': 0.000, 'rotate_to': (0.000, 79.676, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
         
        }],
        #-VNFA:seq:end:4-#
    ], toSeq7)


def toSeq8(game):
    game.texts_next([
        #-VNFA:seq:start:8-#
        ["SMing", "This is very good, but you seem very tense. There's no reason to be shy.", act, {
            'SNia': {'anim': (1, 4, 0), 'cloth_all': (2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2), 'face_to_full2': 'BAAAAAIAAAAAAAAAuE/Mvfz/f7ESuX4/GPqtvZehn74TX+W8zChyPw==', 'fk_set': {}, 'ik_set': {}, 'kinematic': 0, 'look_at_ptn': 0, 'move_to': (-4.294, 0.008, 52.430), 'rotate_to': (0.000, 275.957, 0.000)},
            'cam': {'goto_pos': ((-4.444, 1.007, 50.750), (0.000, 0.000, -1.533), (6.900, -254.053, 0.000))},
            'STans': {'anim': (1, 4, 0), 'face_to_full2': 'BAAAAAIAAAD+f422/v+Rsvz/f7EAAIA/lJYyvrz9mb0r21q8QFF7Pw==', 'fk_set': {}, 'ik_set': {}, 'kinematic': 0, 'look_at_ptn': 0, 'move_to': (-4.319, -0.023, 51.644), 'rotate_to': (0.000, 269.142, 0.000)},
            'bonr': {'color': (((0.31, 0.31, 0.31, 1.00), (0.80, 0.80, 0.80, 1.00), 0.000, 0.000), ), 'move_to': (-0.005, -0.109, 0.061), 'rotate_to': (359.596, 100.713, 29.567), 'scale_to': (0.346, 1.334, 0.245), 'visible': 1},
            'SLim': {'anim': (1, 4, 0), 'face_to_full2': 'BAAAAAIAAAAAAAAAAAAAAAAAAAAAAIA/SWL0vbadnL79ah69tZpxPw==', 'fk_set': {}, 'ik_set': {}, 'kinematic': 0, 'look_at_ptn': 0, 'move_to': (-4.311, -0.020, 52.098), 'rotate_to': (0.000, 271.405, 0.000)},
            'SJean': {'anim': (1, 4, 0), 'face_to': 4, 'face_to_full2': 'BAAAAAIAAAAAAAAAAAAAAAAAAAAAAIA/WqgtvubdFD7SRc88nHJ5Pw==', 'move_to': (-4.369, 0.016, 51.132), 'rotate_to': (0.000, 276.224, 0.000)},
            'SBoy': {'face_to': 4, 'face_to_full2': 'BAAAAAIAAABc1eo8AukGu/qtdzjv5H8/TDZ7Pb3lary3+GY62n1/Pw==', 'look_at_ptn': 0, 'move_to': (-5.276, -0.001, 51.448), 'rotate_to': (0.000, 94.498, 0.000)},
            'SMing': {'anim': (1, 4, 4), 'face_to_full2': 'BAAAAAIAAAAAAAAAAAAAAAAAAAAAAIA/BNDZvevppj0ZUA88ga59Pw==', 'fk_set': {}, 'ik_set': {}, 'kinematic': 0, 'move_to': (-4.398, -0.006, 50.651), 'rotate_to': (0.000, 290.280, 0.000)},
        }],
        #-VNFA:seq:end:8-#
    ], toSc2_0)

#-VNFA:sel:empty:1-#


def toSc2_0(game):
    load_and_init_scene(game, "fun3.png", init_scene2)
	

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
        toSeq9(game)

    except Exception as e:
        import traceback
        traceback.print_exc()
        toEnd(game, "init_scene FAILED: "+str(e))	


def toSeq9(game):
    game.texts_next([
        #-VNFA:seq:start:9-#
        ["STans", "You like what?", act, {
            'cam': {'goto_pos': ((-6.192, 0.738, 53.020), (0.000, 0.000, -0.771), (-11.900, 142.498, 0.000))},
            'tansinvis': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (2, 10, 4), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 0.000, 'cloth_all': (2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 2), 'cloth_type': 1, 'eyes': 1, 'eyes_blink': 0, 'eyes_open': 1.000, 'face_red': 0.243, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAABbxNQ9/v+DMv3/vzJfnX4/6vtZPj5aD7yA3fk6MB96Pw==', 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {}, 'hands': (11, 11), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {'cf_J_ArmLow01_L': ((-0.535, 1.142, 0.048), ), 'cf_J_ArmLow01_R': ((0.443, 1.147, 0.052), ), 'cf_J_ArmUp00_L': ((-0.073, 1.414, -0.028), ), 'cf_J_ArmUp00_R': ((0.089, 1.384, -0.038), ), 'cf_J_Foot01_L': ((-0.100, 0.066, -0.055), (1.022, 358.251, 354.118)), 'cf_J_Foot01_R': ((0.141, 0.066, -0.024), (359.986, 0.232, 0.000)), 'cf_J_Hand_L': ((-0.071, 1.247, -0.115), (53.460, 11.000, 190.680)), 'cf_J_Hand_R': ((0.095, 1.222, -0.122), (57.443, 323.691, 149.466)), 'cf_J_Hips': ((0.009, 1.046, 0.033), ), 'cf_J_LegLow01_L': ((-0.014, 0.498, -0.497), ), 'cf_J_LegLow01_R': ((0.047, 0.507, 0.727), ), 'cf_J_LegUp00_L': ((-0.053, 0.945, 0.009), ), 'cf_J_LegUp00_R': ((0.095, 0.929, -0.003), )}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 1, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 1, 'mouth_open': 0.000, 'move_to': (-5.060, 0.939, 51.121), 'nip_stand': 0.000, 'rotate_to': (0.000, 269.142, 279.358), 'scale_to': (1.000, 0.500, 0.010), 'skin_tuya': 0.191, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'STans': {'cloth_all': (2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2), 'hands': (0, 11), 'ik_set': {'cf_J_ArmLow01_L': ((-0.131, 1.252, -0.132), ), 'cf_J_ArmLow01_R': ((0.225, 1.168, -0.176), ), 'cf_J_ArmUp00_L': ((-0.073, 1.414, -0.028), ), 'cf_J_ArmUp00_R': ((0.089, 1.384, -0.038), ), 'cf_J_Foot01_L': ((-0.100, 0.066, -0.055), (1.022, 358.251, 354.118)), 'cf_J_Foot01_R': ((0.141, 0.066, -0.024), (359.986, 0.232, 0.000)), 'cf_J_Hand_L': ((-0.205, 0.926, -0.025), (356.838, 336.478, 84.050)), 'cf_J_Hand_R': ((0.319, 1.210, 0.100), (355.599, 298.068, 344.455)), 'cf_J_Hips': ((0.009, 1.046, 0.033), ), 'cf_J_LegLow01_L': ((-0.014, 0.498, 0.063), ), 'cf_J_LegLow01_R': ((0.047, 0.507, 0.092), ), 'cf_J_LegUp00_L': ((-0.053, 0.945, 0.009), ), 'cf_J_LegUp00_R': ((0.095, 0.929, -0.003), )}, 'mouth_open': 0.301},
            'SBoy': {'fk_set': {1: (-21.945, 6.532, -2.949), 2: (-13.030, 6.030, -2.900)}, 'mouth_open': 0.654},
        }],
        #-VNFA:seq:end:9-#
    ], toSeq10)

def toSeq10(game):
    game.texts_next([
        #-VNFA:seq:start:10-#
        ["s", "", act, {
            'cam': {'goto_pos': ((-5.194, 1.074, 51.288), (0.000, 0.000, -2.271), (19.500, 213.048, -70.369))},
            'tansinvis': {'ik_set': {'cf_J_ArmLow01_L': ((-0.535, 1.142, 0.048), ), 'cf_J_ArmLow01_R': ((0.443, 1.147, 0.052), ), 'cf_J_ArmUp00_L': ((-0.073, 1.414, -0.028), ), 'cf_J_ArmUp00_R': ((0.089, 1.384, -0.038), ), 'cf_J_Foot01_L': ((-0.100, 0.066, -0.055), (1.022, 358.251, 354.118)), 'cf_J_Foot01_R': ((0.141, 0.066, -0.024), (359.986, 0.232, 0.000)), 'cf_J_Hand_L': ((-0.071, 1.247, -0.115), (53.460, 11.000, 190.680)), 'cf_J_Hand_R': ((0.095, 1.222, -0.122), (57.443, 323.691, 149.466)), 'cf_J_Hips': ((0.009, 1.046, 0.033), ), 'cf_J_LegLow01_L': ((-0.014, 0.498, -0.497), ), 'cf_J_LegLow01_R': ((0.047, 0.507, 0.727), ), 'cf_J_LegUp00_L': ((-0.053, 0.945, 0.009), ), 'cf_J_LegUp00_R': ((0.095, 0.929, -0.003), )}, 'move_to': (-5.060, 0.939, 51.121), 'rotate_to': (0.000, 269.142, 279.358)},
            'STans': {'ik_set': {'cf_J_ArmLow01_L': ((-0.131, 1.252, -0.132), ), 'cf_J_ArmLow01_R': ((0.225, 1.168, -0.176), ), 'cf_J_ArmUp00_L': ((-0.073, 1.414, -0.028), ), 'cf_J_ArmUp00_R': ((0.089, 1.384, -0.038), ), 'cf_J_Foot01_L': ((-0.100, 0.066, -0.055), (1.022, 358.251, 354.118)), 'cf_J_Foot01_R': ((0.141, 0.066, -0.024), (359.986, 0.232, 0.000)), 'cf_J_Hand_L': ((-0.205, 0.926, -0.025), (356.838, 336.478, 84.050)), 'cf_J_Hand_R': ((0.319, 1.210, 0.100), (355.599, 298.068, 344.455)), 'cf_J_Hips': ((0.009, 1.046, 0.033), ), 'cf_J_LegLow01_L': ((-0.014, 0.498, 0.063), ), 'cf_J_LegLow01_R': ((0.047, 0.507, 0.092), ), 'cf_J_LegUp00_L': ((-0.053, 0.945, 0.009), ), 'cf_J_LegUp00_R': ((0.095, 0.929, -0.003), )}, 'mouth_open': 0.000},
            'SBoy': {'eyes': 11, 'fk_set': {1: (1.570, 5.354, -2.736), 2: (-13.030, 6.030, -2.900)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.114, 0.916, -0.001), ), 'cf_J_ArmLow01_R': ((0.110, 0.907, 0.039), ), 'cf_J_ArmUp00_L': ((-0.113, 1.128, -0.075), ), 'cf_J_ArmUp00_R': ((0.076, 1.111, -0.002), ), 'cf_J_Foot01_L': ((-0.039, 0.065, -0.034), (359.879, 2.310, 0.000)), 'cf_J_Foot01_R': ((0.032, 0.065, -0.024), (359.987, 359.231, 0.000)), 'cf_J_Hand_L': ((-0.055, 0.788, 0.100), (336.069, 84.827, 56.794)), 'cf_J_Hand_R': ((0.011, 0.801, 0.133), (326.854, 266.463, 290.878)), 'cf_J_Hips': ((-0.005, 0.858, -0.003), ), 'cf_J_LegLow01_L': ((-0.056, 0.416, 0.024), ), 'cf_J_LegLow01_R': ((0.047, 0.417, 0.031), ), 'cf_J_LegUp00_L': ((-0.068, 0.733, -0.012), ), 'cf_J_LegUp00_R': ((0.064, 0.735, 0.008), )}, 'kinematic': 3, 'mouth': 9, 'mouth_open': 1.000},
        }],
        ["s", "", act, {
            'cam': {'goto_pos': ((-4.901, 0.791, 53.039), (0.000, 0.000, -1.771), (-2.900, -181.052, 0.000))},
            'tansinvis': {'anim': (0, 2, 1), 'cloth_all': (2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2), 'fk_set': {1: (31.864, -12.419, 6.792), 2: (22.957, -58.201, 0.000)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.465, 1.085, 0.773), ), 'cf_J_ArmLow01_R': ((-0.789, 1.243, 0.376), ), 'cf_J_ArmUp00_L': ((-0.389, 1.060, 0.095), ), 'cf_J_ArmUp00_R': ((-0.490, 1.012, 0.002), ), 'cf_J_Foot01_L': ((-0.285, 0.071, 0.190), (0.905, 184.410, 359.961)), 'cf_J_Foot01_R': ((-0.507, 0.076, 0.415), (10.088, 195.958, 7.816)), 'cf_J_Hand_L': ((-0.248, 0.950, 0.339), (1.619, 193.723, 85.716)), 'cf_J_Hand_R': ((-0.568, 0.960, 0.228), (6.272, 172.757, 283.868)), 'cf_J_Hips': ((-0.397, 0.974, 0.118), ), 'cf_J_LegLow01_L': ((-0.182, 0.336, 0.046), ), 'cf_J_LegLow01_R': ((-0.434, 0.281, 0.159), ), 'cf_J_LegUp00_L': ((-0.354, 0.809, 0.362), ), 'cf_J_LegUp00_R': ((-0.508, 0.806, 0.322), )}, 'kinematic': 3, 'move_to': (-4.747, 0.001, 51.881), 'rotate_to': (0.000, 269.142, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'visible': 0},
            'STans': {'anim': (0, 2, 1), 'fk_set': {1: (31.864, -12.419, 6.792), 2: (22.957, -58.201, 0.000)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.465, 1.085, 0.773), ), 'cf_J_ArmLow01_R': ((-0.789, 1.243, 0.376), ), 'cf_J_ArmUp00_L': ((-0.389, 1.060, 0.095), ), 'cf_J_ArmUp00_R': ((-0.490, 1.012, 0.002), ), 'cf_J_Foot01_L': ((-0.285, 0.071, 0.190), (0.905, 184.410, 359.961)), 'cf_J_Foot01_R': ((-0.507, 0.076, 0.415), (10.088, 195.958, 7.816)), 'cf_J_Hand_L': ((-0.248, 0.950, 0.339), (1.619, 193.723, 85.716)), 'cf_J_Hand_R': ((-0.568, 0.960, 0.228), (6.272, 172.757, 283.868)), 'cf_J_Hips': ((-0.397, 0.974, 0.118), ), 'cf_J_LegLow01_L': ((-0.182, 0.336, 0.046), ), 'cf_J_LegLow01_R': ((-0.434, 0.281, 0.159), ), 'cf_J_LegUp00_L': ((-0.354, 0.809, 0.362), ), 'cf_J_LegUp00_R': ((-0.508, 0.806, 0.322), )}, 'kinematic': 3, 'look_at_ptn': 3, 'move_to': (-4.747, 0.001, 51.881)},
            'SBoy': {'ik_set': {'cf_J_ArmLow01_L': ((-0.114, 0.916, -0.001), ), 'cf_J_ArmLow01_R': ((0.110, 0.907, 0.039), ), 'cf_J_ArmUp00_L': ((-0.113, 1.128, -0.075), ), 'cf_J_ArmUp00_R': ((0.076, 1.111, -0.002), ), 'cf_J_Foot01_L': ((-0.039, 0.065, -0.034), (359.879, 2.310, 0.000)), 'cf_J_Foot01_R': ((0.032, 0.065, -0.024), (359.987, 359.231, 0.000)), 'cf_J_Hand_L': ((-0.115, 0.788, 0.051), (336.069, 84.827, 56.794)), 'cf_J_Hand_R': ((0.015, 0.806, 0.092), (326.854, 266.463, 290.878)), 'cf_J_Hips': ((-0.005, 0.858, -0.003), ), 'cf_J_LegLow01_L': ((-0.056, 0.416, 0.024), ), 'cf_J_LegLow01_R': ((0.047, 0.417, 0.031), ), 'cf_J_LegUp00_L': ((-0.068, 0.733, -0.012), ), 'cf_J_LegUp00_R': ((0.064, 0.735, 0.008), )}},
        }],
        ["s", "", act, {
            'cam': {'goto_pos': ((-5.354, 1.153, 52.795), (0.000, 0.000, -1.793), (12.450, 161.898, 0.000))},
            'tansinvis': {'anim': (5, 67, 0), 'fk_set': {1: (28.974, 4.529, 15.422), 2: (-7.112, -43.214, 2.036)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.465, 1.085, 0.773), ), 'cf_J_ArmLow01_R': ((-0.789, 1.243, 0.376), ), 'cf_J_ArmUp00_L': ((-0.374, 0.986, 0.109), ), 'cf_J_ArmUp00_R': ((-0.542, 0.926, 0.074), ), 'cf_J_Foot01_L': ((-0.285, 0.071, 0.190), (0.905, 184.410, 359.961)), 'cf_J_Foot01_R': ((-0.446, 0.073, 0.212), (10.088, 195.958, 7.816)), 'cf_J_Hand_L': ((-0.237, 0.727, 0.229), (1.619, 193.723, 85.716)), 'cf_J_Hand_R': ((-0.603, 0.749, 0.271), (6.272, 172.757, 283.868)), 'cf_J_Hips': ((-0.397, 0.974, 0.118), ), 'cf_J_LegLow01_L': ((-0.306, 0.340, 0.036), ), 'cf_J_LegLow01_R': ((-0.461, 0.281, -0.157), ), 'cf_J_LegUp00_L': ((-0.354, 0.809, 0.362), ), 'cf_J_LegUp00_R': ((-0.508, 0.806, 0.322), )}, 'move_to': (-4.747, 0.001, 51.893)},
            'STans': {'anim': (5, 67, 0), 'cloth_all': (2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 2), 'fk_set': {1: (28.974, 4.529, 15.422), 2: (-7.112, -43.214, 2.036)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.465, 1.085, 0.773), ), 'cf_J_ArmLow01_R': ((-0.789, 1.243, 0.376), ), 'cf_J_ArmUp00_L': ((-0.374, 0.986, 0.109), ), 'cf_J_ArmUp00_R': ((-0.542, 0.926, 0.074), ), 'cf_J_Foot01_L': ((-0.285, 0.071, 0.190), (0.905, 184.410, 359.961)), 'cf_J_Foot01_R': ((-0.446, 0.073, 0.212), (10.088, 195.958, 7.816)), 'cf_J_Hand_L': ((-0.238, 0.763, 0.263), (1.619, 193.723, 85.716)), 'cf_J_Hand_R': ((-0.603, 0.749, 0.271), (6.272, 172.757, 283.868)), 'cf_J_Hips': ((-0.397, 0.974, 0.118), ), 'cf_J_LegLow01_L': ((-0.306, 0.340, 0.036), ), 'cf_J_LegLow01_R': ((-0.461, 0.281, -0.157), ), 'cf_J_LegUp00_L': ((-0.354, 0.809, 0.362), ), 'cf_J_LegUp00_R': ((-0.508, 0.806, 0.322), )}},
            'SBoy': {'fk_set': {1: (19.100, 4.481, -2.894), 2: (-6.039, 5.675, -2.841)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.114, 0.916, -0.001), ), 'cf_J_ArmLow01_R': ((0.110, 0.907, 0.039), ), 'cf_J_ArmUp00_L': ((-0.113, 1.128, -0.075), ), 'cf_J_ArmUp00_R': ((0.076, 1.111, -0.002), ), 'cf_J_Foot01_L': ((-0.039, 0.065, -0.034), (359.879, 2.310, 0.000)), 'cf_J_Foot01_R': ((0.032, 0.065, -0.024), (359.987, 359.231, 0.000)), 'cf_J_Hand_L': ((-0.115, 0.788, 0.051), (336.069, 84.827, 56.794)), 'cf_J_Hand_R': ((0.099, 0.795, 0.064), (326.854, 266.463, 290.878)), 'cf_J_Hips': ((-0.005, 0.858, -0.003), ), 'cf_J_LegLow01_L': ((-0.056, 0.416, 0.024), ), 'cf_J_LegLow01_R': ((0.047, 0.417, 0.031), ), 'cf_J_LegUp00_L': ((-0.068, 0.733, -0.012), ), 'cf_J_LegUp00_R': ((0.064, 0.735, 0.008), )}},
        }],
        ["s", "", act, {
            'cam': {'goto_pos': ((-5.260, 0.801, 52.420), (0.000, 0.000, -2.021), (-0.950, 168.748, 0.000))},
            'tansinvis': {'cloth_all': (2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 2), 'fk_set': {1: (12.838, 43.913, 30.121), 2: (-7.112, -43.214, 2.036)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.465, 1.085, 0.773), ), 'cf_J_ArmLow01_R': ((-0.789, 1.243, 0.376), ), 'cf_J_ArmUp00_L': ((-0.275, 0.755, -0.080), ), 'cf_J_ArmUp00_R': ((-0.472, 0.762, -0.079), ), 'cf_J_Foot01_L': ((-0.275, 0.071, 0.149), (0.905, 184.410, 359.961)), 'cf_J_Foot01_R': ((-0.457, 0.057, 0.103), (10.088, 195.958, 7.816)), 'cf_J_Hand_L': ((-0.224, 0.274, 0.223), (1.619, 193.723, 85.716)), 'cf_J_Hand_R': ((-0.556, 0.166, 0.200), (6.272, 172.757, 283.868)), 'cf_J_Hips': ((-0.343, 0.852, 0.030), ), 'cf_J_LegLow01_L': ((-0.284, 0.340, -0.120), ), 'cf_J_LegLow01_R': ((-0.461, 0.281, -0.157), ), 'cf_J_LegUp00_L': ((-0.395, 0.891, 0.341), ), 'cf_J_LegUp00_R': ((-0.536, 0.888, 0.319), )}, 'move_to': (-4.861, -0.453, 52.095), 'rotate_to': (0.000, 269.142, 12.016), 'scale_to': (1.000, 1.000, 0.655), 'visible': 1},
            'STans': {'cloth_all': (2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2), 'fk_set': {1: (12.838, 43.913, 30.121), 2: (-7.112, -43.214, 2.036)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.465, 1.085, 0.773), ), 'cf_J_ArmLow01_R': ((-0.789, 1.243, 0.376), ), 'cf_J_ArmUp00_L': ((-0.275, 0.755, -0.080), ), 'cf_J_ArmUp00_R': ((-0.545, 0.764, -0.083), ), 'cf_J_Foot01_L': ((-0.275, 0.071, 0.149), (0.905, 184.410, 359.961)), 'cf_J_Foot01_R': ((-0.455, 0.059, 0.105), (10.088, 195.958, 7.816)), 'cf_J_Hand_L': ((-0.224, 0.274, 0.223), (1.619, 193.723, 85.716)), 'cf_J_Hand_R': ((-0.557, 0.168, 0.203), (6.272, 172.757, 283.868)), 'cf_J_Hips': ((-0.384, 0.853, 0.027), ), 'cf_J_LegLow01_L': ((-0.284, 0.340, -0.120), ), 'cf_J_LegLow01_R': ((-0.461, 0.281, -0.157), ), 'cf_J_LegUp00_L': ((-0.285, 0.884, 0.341), ), 'cf_J_LegUp00_R': ((-0.530, 0.882, 0.344), )}, 'move_to': (-4.870, 0.001, 51.881)},
            'SBoy': {'fk_set': {1: (35.565, 3.472, -3.362), 2: (-6.039, 5.675, -2.841)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.200, 0.953, -0.309), ), 'cf_J_ArmLow01_R': ((0.110, 0.907, 0.039), ), 'cf_J_ArmUp00_L': ((-0.149, 1.101, -0.296), ), 'cf_J_ArmUp00_R': ((0.070, 1.088, -0.058), ), 'cf_J_Foot01_L': ((-0.039, 0.057, 0.033), (359.879, 2.310, 0.000)), 'cf_J_Foot01_R': ((0.032, 0.065, -0.024), (359.987, 359.231, 0.000)), 'cf_J_Hand_L': ((-0.184, 1.077, -0.284), (336.069, 84.827, 232.344)), 'cf_J_Hand_R': ((0.099, 0.795, 0.064), (326.854, 266.463, 290.878)), 'cf_J_Hips': ((-0.016, 0.853, -0.026), ), 'cf_J_LegLow01_L': ((-0.056, 0.416, 0.024), ), 'cf_J_LegLow01_R': ((0.047, 0.417, 0.031), ), 'cf_J_LegUp00_L': ((-0.068, 0.733, -0.012), ), 'cf_J_LegUp00_R': ((0.064, 0.735, 0.008), )}},
        }],
        ["SBoy", "Ghaa...", act, {
            'cam': {'goto_pos': ((-4.934, 0.970, 52.019), (0.000, 0.000, -2.053), (-5.700, 204.698, 0.000))},
            'SBoy': {'look_at_ptn': 3},
        }],
        ["SBoy", "wahhhhh", act, {
            'SNia': {'acc_all': (1, 1, 0, 1, 0, 0, 1, 1, 1, 1), 'face_to_full2': 'BAAAAAIAAAAAAAAAAAAAAAAAAAAAAIA/KZqAPG6kYr4biGk77Z15Pw==', 'hands': (1, 7), 'ik_set': {'cf_J_ArmLow01_L': ((-0.164, 0.695, 0.023), ), 'cf_J_ArmLow01_R': ((0.104, 0.917, 0.026), ), 'cf_J_ArmUp00_L': ((-0.120, 0.945, -0.021), ), 'cf_J_ArmUp00_R': ((0.087, 0.898, 0.005), ), 'cf_J_Foot01_L': ((-0.076, 0.077, 0.505), (359.777, 350.154, 2.118)), 'cf_J_Foot01_R': ((0.034, 0.077, 0.536), (358.740, 351.135, 355.462)), 'cf_J_Hand_L': ((-0.076, 0.599, 0.177), (340.569, 118.619, 0.310)), 'cf_J_Hand_R': ((-0.024, 0.899, 0.164), (329.437, 58.200, 103.517)), 'cf_J_Hips': ((0.000, 0.651, 0.000), ), 'cf_J_LegLow01_L': ((-0.084, 0.493, 0.393), ), 'cf_J_LegLow01_R': ((0.042, 0.485, 0.395), ), 'cf_J_LegUp00_L': ((-0.083, 0.503, 0.006), ), 'cf_J_LegUp00_R': ((0.079, 0.500, 0.010), )}, 'kinematic': 1, 'mouth': 0, 'mouth_open': 0.610},
            'cam': {'goto_pos': ((-7.789, 1.148, 49.538), (0.000, 0.000, -1.198), (5.100, 56.498, 0.000))},
            'STans': {'anim': (2, 8, 0), 'face_red': 0.089, 'fk_set': {1: (31.864, -12.419, 6.792), 2: (4.487, -58.201, 0.000)}, 'hands': (0, 0), 'ik_set': {'cf_J_ArmLow01_L': ((-0.968, 1.041, 0.531), ), 'cf_J_ArmLow01_R': ((-0.789, 1.243, 0.376), ), 'cf_J_ArmUp00_L': ((-0.383, 1.297, 0.187), ), 'cf_J_ArmUp00_R': ((-0.499, 1.479, -0.124), ), 'cf_J_Foot01_L': ((-0.233, 0.070, 0.216), (0.626, 140.565, 359.346)), 'cf_J_Foot01_R': ((-0.409, 0.119, 0.129), (10.503, 156.030, 359.593)), 'cf_J_Hand_L': ((-0.272, 0.948, 0.343), (355.476, 91.996, 62.295)), 'cf_J_Hand_R': ((-0.494, 0.873, -0.055), (353.696, 109.953, 285.702)), 'cf_J_Hips': ((-0.379, 0.991, 0.154), ), 'cf_J_LegLow01_L': ((-0.121, 0.354, 0.092), ), 'cf_J_LegLow01_R': ((-0.158, 0.501, -0.284), ), 'cf_J_LegUp00_L': ((-0.354, 0.809, 0.362), ), 'cf_J_LegUp00_R': ((-0.504, 0.830, -0.018), )}, 'mouth': 0, 'mouth_open': 0.404, 'skin_tuya': 0.132},
            'SLim': {'face_to_full2': 'BAAAAAIAAAAAAAAAAAAAAAAAAAAAAIA/1mh2PJU/C77dTQc7nZd9Pw==', 'mouth': 0, 'mouth_open': 0.250},
            'SJean': {'face_to_full2': 'BAAAAAIAAAAAAAAAAAAAAAAAAAAAAIA/OxwHuwSAST349tQ4g7B/Pw==', 'fk_set': {1: (-40.662, 14.223, -17.738), 2: (-28.801, 8.871, -10.104)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.166, 0.700, 0.024), ), 'cf_J_ArmLow01_R': ((0.158, 0.703, 0.018), ), 'cf_J_ArmUp00_L': ((-0.118, 0.932, 0.260), ), 'cf_J_ArmUp00_R': ((0.087, 0.934, 0.345), ), 'cf_J_Foot01_L': ((-0.109, 0.076, 0.263), (359.783, 350.164, 2.122)), 'cf_J_Foot01_R': ((0.033, 0.076, 0.528), (358.735, 351.138, 355.465)), 'cf_J_Hand_L': ((-0.217, 0.577, 0.151), (340.521, 118.598, 0.277)), 'cf_J_Hand_R': ((0.059, 0.919, 0.748), (333.090, 269.665, 14.177)), 'cf_J_Hips': ((0.000, 0.785, 0.075), ), 'cf_J_LegLow01_L': ((-0.083, 0.486, 0.387), ), 'cf_J_LegLow01_R': ((0.041, 0.478, 0.389), ), 'cf_J_LegUp00_L': ((-0.082, 0.496, 0.006), ), 'cf_J_LegUp00_R': ((0.078, 0.493, 0.010), )}, 'kinematic': 3, 'mouth': 0, 'mouth_open': 0.346},
            'SBoy': {'fk_set': {1: (35.565, 3.472, -3.362), 2: (-37.957, -16.862, -0.369)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.200, 0.953, -0.309), ), 'cf_J_ArmLow01_R': ((0.118, 0.918, -0.160), ), 'cf_J_ArmUp00_L': ((-0.150, 1.097, -0.293), ), 'cf_J_ArmUp00_R': ((0.070, 1.088, -0.058), ), 'cf_J_Foot01_L': ((-0.034, 0.178, 0.253), (359.879, 2.310, 0.000)), 'cf_J_Foot01_R': ((0.026, 0.108, 0.086), (359.987, 359.231, 0.000)), 'cf_J_Hand_L': ((-0.165, 0.916, -0.498), (8.916, 283.090, 312.905)), 'cf_J_Hand_R': ((0.300, 0.995, 0.000), (277.239, 254.416, 115.697)), 'cf_J_Hips': ((-0.005, 0.837, -0.086), ), 'cf_J_LegLow01_L': ((-0.193, 0.382, 0.571), ), 'cf_J_LegLow01_R': ((0.024, 0.427, 0.372), ), 'cf_J_LegUp00_L': ((-0.068, 0.733, -0.012), ), 'cf_J_LegUp00_R': ((0.064, 0.735, 0.008), )}, 'rotate_to': (332.298, 94.498, 0.000)},
            'tansinvis': {'ik_set': {'cf_J_ArmLow01_L': ((-0.465, 1.085, 0.773), ), 'cf_J_ArmLow01_R': ((-0.718, 1.340, 0.229), ), 'cf_J_ArmUp00_L': ((-0.275, 0.755, -0.080), ), 'cf_J_ArmUp00_R': ((-0.472, 0.762, -0.079), ), 'cf_J_Foot01_L': ((-0.275, 0.071, 0.149), (0.905, 184.410, 359.961)), 'cf_J_Foot01_R': ((-0.457, 0.057, 0.103), (10.088, 195.958, 7.816)), 'cf_J_Hand_L': ((-0.224, 0.274, 0.223), (1.619, 193.723, 85.716)), 'cf_J_Hand_R': ((-0.556, 0.166, 0.200), (6.272, 172.757, 283.868)), 'cf_J_Hips': ((-0.343, 0.852, 0.030), ), 'cf_J_LegLow01_L': ((-0.284, 0.340, -0.120), ), 'cf_J_LegLow01_R': ((-0.461, 0.281, -0.157), ), 'cf_J_LegUp00_L': ((-0.395, 0.888, 0.345), ), 'cf_J_LegUp00_R': ((-0.525, 0.883, 0.316), )}, 'move_to': (-4.824, -0.642, 52.072), 'rotate_to': (355.458, 291.057, 11.136)},
            'SMing': {'face_to_full2': 'BAAAAAIAAAAAAAAAAAAAAAAAAAAAAIA/UmhEPfSAjzv9b1y5+7N/Pw==', 'mouth': 0, 'mouth_open': 0.610},
        }],
        ["SBoy", "Oooofff!", act, {
            'cam': {'goto_pos': ((-4.975, 1.085, 51.734), (0.000, 0.000, -0.868), (36.350, 249.898, 0.000))},
            'SBoy': {'anim': (1, 5, 0), 'eyes': 0, 'eyes_open': 0.000, 'fk_set': {1: (-13.594, 6.091, -2.813), 2: (-14.646, -17.012, -0.300)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.162, 0.028, -0.176), ), 'cf_J_ArmLow01_R': ((0.158, 0.028, -0.182), ), 'cf_J_ArmUp00_L': ((-0.098, 0.050, -0.366), ), 'cf_J_ArmUp00_R': ((0.092, 0.053, -0.370), ), 'cf_J_Foot01_L': ((-0.084, 0.035, 0.632), (282.167, 23.496, 341.195)), 'cf_J_Foot01_R': ((0.215, 0.047, 0.656), (297.251, 327.848, 44.004)), 'cf_J_Hand_L': ((-0.156, 0.032, -0.661), (347.669, 45.746, 166.701)), 'cf_J_Hand_R': ((0.336, 0.005, -0.372), (354.275, 223.491, 198.020)), 'cf_J_Hips': ((-0.016, 0.070, -0.145), ), 'cf_J_LegLow01_L': ((-0.079, 0.072, 0.322), ), 'cf_J_LegLow01_R': ((0.133, 0.073, 0.311), ), 'cf_J_LegUp00_L': ((-0.073, 0.080, 0.003), ), 'cf_J_LegUp00_R': ((0.061, 0.081, 0.000), )}, 'mouth': 12, 'mouth_open': 0.000, 'move_to': (-5.938, 0.022, 51.462), 'rotate_to': (3.194, 94.498, 0.000)},
        }],
        ["SBoy", "Huh, what happened?", act, {
            'SNia': {'anim': (1, 3, 21), 'face_to_full2': 'BAAAAAIAAAApCVw+AcBgsgEA4LIhBXo/otlaPgJY2T2tYr+8dYh4Pw==', 'ik_set': {'cf_J_ArmLow01_L': ((-0.240, 1.105, -0.199), ), 'cf_J_ArmLow01_R': ((0.158, 1.122, -0.235), ), 'cf_J_ArmUp00_L': ((-0.158, 1.333, -0.126), ), 'cf_J_ArmUp00_R': ((0.070, 1.346, -0.147), ), 'cf_J_Foot01_L': ((-0.205, 0.077, -0.209), (359.663, 4.120, 0.623)), 'cf_J_Foot01_R': ((0.046, 0.077, -0.237), (359.758, 7.037, 359.470)), 'cf_J_Hand_L': ((-0.113, 1.093, -0.058), (300.807, 124.657, 17.764)), 'cf_J_Hand_R': ((0.064, 1.107, -0.048), (294.603, 247.212, 325.242)), 'cf_J_Hips': ((-0.033, 1.037, -0.147), ), 'cf_J_LegLow01_L': ((-0.164, 0.403, -0.011), ), 'cf_J_LegLow01_R': ((0.049, 0.504, -0.175), ), 'cf_J_LegUp00_L': ((-0.115, 0.889, -0.173), ), 'cf_J_LegUp00_R': ((0.047, 0.891, -0.184), )}, 'look_at_ptn': 3, 'move_to': (-6.104, -0.012, 51.652), 'rotate_to': (0.000, 203.385, 0.000)},
            'cam': {'goto_pos': ((-6.430, 0.202, 51.510), (0.000, 0.000, 0.000), (-0.650, -264.052, 0.000))},
            'STans': {'anim': (4, 49, 0), 'fk_set': {1: (6.316, 1.033, 0.553), 2: (-25.884, 0.706, 0.611)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.277, 0.731, -0.008), ), 'cf_J_ArmLow01_R': ((0.266, 0.728, -0.008), ), 'cf_J_ArmUp00_L': ((-0.113, 0.640, 0.207), ), 'cf_J_ArmUp00_R': ((0.138, 0.585, 0.287), ), 'cf_J_Foot01_L': ((-0.171, 0.099, -0.383), (69.491, 218.776, 205.221)), 'cf_J_Foot01_R': ((0.200, 0.091, -0.361), (69.490, 141.222, 154.778)), 'cf_J_Hand_L': ((-0.231, 0.150, 0.196), (14.642, 80.156, 15.453)), 'cf_J_Hand_R': ((0.158, 0.201, 0.395), (328.143, 0.892, 287.921)), 'cf_J_Hips': ((-0.035, 0.449, -0.074), ), 'cf_J_LegLow01_L': ((-0.149, 0.026, -0.044), ), 'cf_J_LegLow01_R': ((0.125, 0.034, -0.020), ), 'cf_J_LegUp00_L': ((-0.109, 0.294, -0.264), ), 'cf_J_LegUp00_R': ((0.061, 0.296, -0.261), )}, 'move_to': (-6.654, -0.023, 51.959), 'rotate_to': (0.000, 151.173, 0.000)},
            'SLim': {'anim': (2, 10, 2), 'face_to_full2': 'BAAAAAIAAAAQMAg+9v9/Mfn/rzPSuX0/n5kfPkhrprv7FVI6Od58Pw==', 'look_at_ptn': 3, 'move_to': (-5.275, -0.020, 51.641), 'rotate_to': (0.000, 258.507, 0.000)},
            'SJean': {'anim': (2, 11, 1), 'face_to_full2': 'BAAAAAIAAAAmrVw+/f+FMv3/jzMZ/Hk/x75ZPvQvIr6hKg890Kx2Pw==', 'fk_set': {}, 'ik_set': {}, 'kinematic': 0, 'look_at_ptn': 3, 'move_to': (-5.696, 0.016, 51.132), 'rotate_to': (0.000, 312.106, 0.000)},
            'tansinvis': {'move_to': (-6.838, 0.086, 51.391), 'rotate_to': (283.982, 297.487, 232.081), 'scale_to': (0.941, 1.009, 0.349)},
            'SMing': {'anim': (2, 12, 3), 'face_to_full2': 'BAAAAAIAAAAjcCc+/r8Vsvz/fzH1jXw/UAszPvqCfr0nKTU8wIl7Pw==', 'ik_set': {'cf_J_ArmLow01_L': ((-0.176, 1.128, 0.183), ), 'cf_J_ArmLow01_R': ((0.088, 1.102, 0.199), ), 'cf_J_ArmUp00_L': ((-0.210, 1.314, 0.054), ), 'cf_J_ArmUp00_R': ((0.046, 1.309, 0.080), ), 'cf_J_Foot01_L': ((-0.114, 0.080, -0.042), (358.304, 8.987, 359.267)), 'cf_J_Foot01_R': ((0.106, 0.080, -0.110), (359.187, 353.095, 1.732)), 'cf_J_Hand_L': ((-0.139, 1.217, 0.162), (350.829, 202.172, 249.175)), 'cf_J_Hand_R': ((0.006, 1.244, 0.185), (0.593, 150.595, 77.518)), 'cf_J_Hips': ((-0.029, 1.042, 0.047), ), 'cf_J_LegLow01_L': ((-0.078, 0.505, 0.060), ), 'cf_J_LegLow01_R': ((0.083, 0.501, 0.011), ), 'cf_J_LegUp00_L': ((-0.079, 0.893, -0.007), ), 'cf_J_LegUp00_R': ((0.086, 0.894, -0.006), )}, 'kinematic': 1, 'look_at_ptn': 3, 'move_to': (-6.326, -0.006, 51.194), 'rotate_to': (0.000, 353.040, 0.000)},
        }],
        #-VNFA:seq:end:10-#
    ], toSeq11)

def toSeq11(game):
    game.texts_next([
        #-VNFA:seq:start:11-#
        ["s", "", act, {
            'SNia': {'acc_all': (1, 1, 0, 1, 0, 0, 1, 1, 1, 1), 'anim': (1, 3, 21), 'eyes_blink': 1, 'face_to_full2': 'BAAAAAIAAAApCVw+AcBgsgEA4LIhBXo/otlaPgJY2T2tYr+8dYh4Pw==', 'hands': (1, 7), 'ik_set': {'cf_J_ArmLow01_L': ((-0.240, 1.105, -0.199), ), 'cf_J_ArmLow01_R': ((0.158, 1.122, -0.235), ), 'cf_J_ArmUp00_L': ((-0.158, 1.333, -0.126), ), 'cf_J_ArmUp00_R': ((0.070, 1.346, -0.147), ), 'cf_J_Foot01_L': ((-0.205, 0.077, -0.209), (359.663, 4.120, 0.623)), 'cf_J_Foot01_R': ((0.046, 0.077, -0.237), (359.758, 7.037, 359.470)), 'cf_J_Hand_L': ((-0.113, 1.093, -0.058), (300.807, 124.657, 17.764)), 'cf_J_Hand_R': ((0.124, 1.111, -0.064), (294.603, 247.212, 325.242)), 'cf_J_Hips': ((-0.033, 1.037, -0.147), ), 'cf_J_LegLow01_L': ((-0.164, 0.403, -0.011), ), 'cf_J_LegLow01_R': ((0.049, 0.504, -0.175), ), 'cf_J_LegUp00_L': ((-0.115, 0.889, -0.173), ), 'cf_J_LegUp00_R': ((0.047, 0.891, -0.184), )}, 'kinematic': 1, 'look_at_ptn': 3, 'mouth': 0, 'mouth_open': 0.610, 'move_to': (-6.104, -0.012, 51.652), 'rotate_to': (0.000, 203.385, 0.000)},
            'cam': {'goto_pos': ((-7.646, 1.373, 49.448), (0.000, 0.000, -0.970), (9.750, 29.147, 0.000))},
            'STans': {'anim': (3, 35, 0), 'cloth_all': (2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2), 'eyes_blink': 1, 'face_red': 0.089, 'fk_set': {1: (20.897, 1.182, 0.588), 2: (33.455, 1.336, 0.659)}, 'hands': (0, 0), 'ik_set': {'cf_J_ArmLow01_L': ((-0.281, 1.208, 0.010), ), 'cf_J_ArmLow01_R': ((0.205, 1.216, -0.009), ), 'cf_J_ArmUp00_L': ((-0.114, 1.374, -0.144), ), 'cf_J_ArmUp00_R': ((0.117, 1.369, -0.107), ), 'cf_J_Foot01_L': ((-0.064, 0.083, -0.175), (358.099, 5.052, 4.540)), 'cf_J_Foot01_R': ((0.080, 0.083, -0.219), (10.017, 357.469, 356.700)), 'cf_J_Hand_L': ((-0.091, 1.067, 0.140), (319.860, 125.423, 60.045)), 'cf_J_Hand_R': ((0.027, 1.275, 0.149), (305.471, 153.288, 34.990)), 'cf_J_Hips': ((-0.003, 1.074, -0.063), ), 'cf_J_LegLow01_L': ((-0.068, 0.525, -0.099), ), 'cf_J_LegLow01_R': ((0.077, 0.523, -0.137), ), 'cf_J_LegUp00_L': ((-0.085, 0.921, -0.107), ), 'cf_J_LegUp00_R': ((0.085, 0.919, -0.107), )}, 'kinematic': 3, 'look_at_ptn': 3, 'mouth': 0, 'mouth_open': 0.404, 'move_to': (-6.420, -0.023, 51.607), 'rotate_to': (0.000, 128.064, 0.000), 'skin_tuya': 0.132},
            'SLim': {'anim': (2, 10, 2), 'face_to_full2': 'BAAAAAIAAAAQMAg+9v9/Mfn/rzPSuX0/n5kfPkhrprv7FVI6Od58Pw==', 'look_at_ptn': 3, 'mouth': 0, 'mouth_open': 0.250, 'move_to': (-5.275, -0.020, 51.641), 'rotate_to': (0.000, 258.507, 0.000)},
            'SJean': {'anim': (2, 11, 1), 'face_to_full2': 'BAAAAAIAAAAmrVw+/f+FMv3/jzMZ/Hk/x75ZPvQvIr6hKg890Kx2Pw==', 'look_at_ptn': 3, 'mouth': 0, 'mouth_open': 0.346, 'move_to': (-5.696, 0.016, 51.132), 'rotate_to': (0.000, 312.106, 0.000)},
            'SBoy': {'anim': (2, 11, 0), 'eyes': 0, 'eyes_blink': 1, 'fk_set': {1: (-13.890, -63.449, -21.603), 2: (-28.067, -16.933, -0.328)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.136, 0.909, -0.050), ), 'cf_J_ArmLow01_R': ((0.135, 0.906, -0.038), ), 'cf_J_ArmUp00_L': ((-0.109, 1.093, 0.048), ), 'cf_J_ArmUp00_R': ((0.082, 1.101, 0.076), ), 'cf_J_Foot01_L': ((-0.121, 0.065, -0.034), (358.826, 7.166, 0.000)), 'cf_J_Foot01_R': ((0.077, 0.065, -0.024), (359.229, 354.184, 0.000)), 'cf_J_Hand_L': ((-0.183, 0.743, -0.027), (0.217, 6.753, 57.283)), 'cf_J_Hand_R': ((0.184, 0.743, -0.008), (2.985, 0.000, 304.646)), 'cf_J_Hips': ((-0.007, 0.849, 0.072), ), 'cf_J_LegLow01_L': ((-0.087, 0.412, 0.037), ), 'cf_J_LegLow01_R': ((0.068, 0.414, 0.047), ), 'cf_J_LegUp00_L': ((-0.066, 0.731, 0.019), ), 'cf_J_LegUp00_R': ((0.068, 0.732, 0.019), )}, 'kinematic': 3, 'look_at_ptn': 3, 'mouth': 0, 'mouth_open': 0.000, 'move_to': (-6.364, 0.022, 51.567), 'rotate_to': (357.600, 315.806, 357.892)},
            'tansinvis': {'anim': (5, 67, 0), 'cloth_all': (2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 2), 'fk_set': {1: (12.838, 43.913, 30.121), 2: (-7.112, -43.214, 2.036)}, 'ik_set': {'cf_J_ArmLow01_L': ((-0.465, 1.085, 0.773), ), 'cf_J_ArmLow01_R': ((-0.718, 1.340, 0.229), ), 'cf_J_ArmUp00_L': ((-0.275, 0.755, -0.080), ), 'cf_J_ArmUp00_R': ((-0.472, 0.762, -0.079), ), 'cf_J_Foot01_L': ((-0.275, 0.071, 0.149), (0.905, 184.410, 359.961)), 'cf_J_Foot01_R': ((-0.457, 0.057, 0.103), (10.088, 195.958, 7.816)), 'cf_J_Hand_L': ((-0.224, 0.274, 0.223), (1.619, 193.723, 85.716)), 'cf_J_Hand_R': ((-0.556, 0.166, 0.200), (6.272, 172.757, 283.868)), 'cf_J_Hips': ((-0.343, 0.852, 0.030), ), 'cf_J_LegLow01_L': ((-0.284, 0.340, -0.120), ), 'cf_J_LegLow01_R': ((-0.461, 0.281, -0.157), ), 'cf_J_LegUp00_L': ((-0.395, 0.888, 0.345), ), 'cf_J_LegUp00_R': ((-0.525, 0.883, 0.316), )}, 'kinematic': 3, 'move_to': (-6.838, 0.086, 51.391), 'rotate_to': (283.982, 297.487, 232.081), 'scale_to': (0.941, 1.009, 0.349)},
            'SMing': {'anim': (2, 12, 3), 'face_to_full2': 'BAAAAAIAAAAjcCc+/r8Vsvz/fzH1jXw/UAszPvqCfr0nKTU8wIl7Pw==', 'ik_set': {'cf_J_ArmLow01_L': ((-0.176, 1.128, 0.183), ), 'cf_J_ArmLow01_R': ((0.088, 1.102, 0.199), ), 'cf_J_ArmUp00_L': ((-0.210, 1.314, 0.054), ), 'cf_J_ArmUp00_R': ((0.046, 1.309, 0.080), ), 'cf_J_Foot01_L': ((-0.114, 0.080, -0.042), (358.304, 8.987, 359.267)), 'cf_J_Foot01_R': ((0.106, 0.080, -0.110), (359.187, 353.095, 1.732)), 'cf_J_Hand_L': ((-0.139, 1.217, 0.162), (350.829, 202.172, 249.175)), 'cf_J_Hand_R': ((0.006, 1.244, 0.185), (0.593, 150.595, 77.518)), 'cf_J_Hips': ((-0.029, 1.042, 0.047), ), 'cf_J_LegLow01_L': ((-0.078, 0.505, 0.060), ), 'cf_J_LegLow01_R': ((0.083, 0.501, 0.011), ), 'cf_J_LegUp00_L': ((-0.079, 0.893, -0.007), ), 'cf_J_LegUp00_R': ((0.086, 0.894, -0.006), )}, 'kinematic': 1, 'look_at_ptn': 3, 'mouth': 0, 'mouth_open': 0.610, 'move_to': (-6.326, -0.006, 50.832), 'rotate_to': (0.000, 353.040, 0.000)},
        }],
        #-VNFA:seq:end:11-#
    ], toSeq12)

def toSeq12(game):
    game.texts_next([
        #-VNFA:seq:empty:12-#
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
