#vngame;neo;fun1
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
    if enableQuickReload and hasattr(game, "scenePNG") and game.scenePNG == "fun1.png":
        # skip load png, quick reload
        # all actor/prop status must be reset by script
        init_scene(game)
    else:
        load_and_init_scene(game, "fun1.png", init_scene)
    
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
        ["s", "", act, {
            'cam': {'goto_pos': ((-11.537, 9.101, 4.490), (0.000, 0.000, -6.699), (12.540, 166.001, 0.000))},
            'Kassandra': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (0, 0, 0), 'anim_lp': 1, 'anim_ptn': 0.000, 'anim_spd': 0.596, 'cloth_all': (0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0), 'cloth_type': 0, 'eyes': 9, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full': (4, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 63, 237, 125, 195, 189, 79, 170, 175, 61, 172, 68, 7, 60, 219, 223, 125, 63), 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {}, 'hands': (1, 1), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {'cf_J_ArmLow01_L': ((-0.154, 1.670, 0.193), ), 'cf_J_ArmLow01_R': ((0.234, 1.622, 0.115), ), 'cf_J_ArmUp00_L': ((-0.075, 1.469, -0.038), ), 'cf_J_ArmUp00_R': ((0.183, 1.468, 0.020), ), 'cf_J_Foot01_L': ((-0.191, 0.086, -0.041), (12.924, 3.762, 355.283)), 'cf_J_Foot01_R': ((0.169, 0.086, -0.031), (11.208, 353.872, 0.373)), 'cf_J_Hand_L': ((0.065, 1.869, 0.034), (3.240, 209.645, 294.548)), 'cf_J_Hand_R': ((0.067, 1.844, 0.005), (28.967, 197.607, 94.925)), 'cf_J_Hips': ((0.065, 1.120, 0.036), ), 'cf_J_LegLow01_L': ((-0.102, 0.541, 0.020), ), 'cf_J_LegLow01_R': ((0.151, 0.546, 0.055), ), 'cf_J_LegUp00_L': ((-0.032, 0.942, -0.016), ), 'cf_J_LegUp00_R': ((0.140, 0.944, 0.020), )}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 1, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 12, 'mouth_open': 0.779, 'move_to': (-10.605, 7.832, 2.355), 'nip_stand': 0.000, 'rotate_to': (0.000, 12.368, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'Bloodsplat': {'move_to': (-10.824, 10.367, 13.264), 'rotate_to': (0.000, 0.000, 0.000), 'visible': 1},
            'Troll': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (9, 167, 0), 'anim_lp': 0, 'anim_ptn': -1.000, 'anim_spd': 0.000, 'cloth_all': (0, 0), 'cloth_type': 0, 'eyes': 4, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_to': 4, 'face_to_full': (4, 0, 0, 0, 2, 0, 0, 0, 136, 32, 56, 61, 0, 0, 0, 50, 0, 0, 0, 0, 193, 189, 127, 63, 99, 177, 33, 62, 229, 238, 110, 190, 58, 105, 29, 61, 184, 110, 117, 63), 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {}, 'hands': (1, 20), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 3, 'mouth_open': 0.346, 'move_to': (-10.553, 7.868, 4.533), 'rotate_to': (0.000, 178.660, 0.000), 'scale_to': (1.201, 1.201, 1.201), 'simple': 0, 'simple_color': (0.00, 0.00, 1.00, 1.00), 'son': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'Zelda': {'acc_all': (1, 1, 1, 0, 1, 0, 1, 1, 0, 0), 'anim': (1, 3, 21), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.000, 'cloth_all': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 'cloth_type': 2, 'eyes': 2, 'eyes_blink': 1, 'eyes_open': 0.713, 'face_red': 0.000, 'face_to': 4, 'face_to_full': (4, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 63, 68, 91, 239, 189, 96, 83, 54, 62, 70, 132, 174, 60, 28, 17, 122, 63), 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {}, 'hands': (1, 1), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {'cf_J_ArmLow01_L': ((-0.098, 1.674, 0.054), ), 'cf_J_ArmLow01_R': ((0.187, 1.604, 0.113), ), 'cf_J_ArmUp00_L': ((-0.075, 1.469, -0.038), ), 'cf_J_ArmUp00_R': ((0.183, 1.468, 0.020), ), 'cf_J_Foot01_L': ((-0.191, 0.086, -0.041), (12.924, 3.762, 355.283)), 'cf_J_Foot01_R': ((0.169, 0.086, -0.031), (11.208, 353.872, 0.373)), 'cf_J_Hand_L': ((0.020, 1.869, 0.034), (3.240, 209.645, 294.548)), 'cf_J_Hand_R': ((0.085, 1.841, -0.004), (28.967, 197.607, 94.925)), 'cf_J_Hips': ((0.065, 1.120, 0.036), ), 'cf_J_LegLow01_L': ((-0.102, 0.541, 0.020), ), 'cf_J_LegLow01_R': ((0.153, 0.547, 0.058), ), 'cf_J_LegUp00_L': ((-0.032, 0.942, -0.016), ), 'cf_J_LegUp00_R': ((0.140, 0.944, 0.020), )}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 1, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 6, 'mouth_open': 0.426, 'move_to': (-11.810, 7.599, 2.345), 'nip_stand': 0.000, 'rotate_to': (0.000, 21.663, 0.000), 'scale_to': (1.100, 1.100, 1.100), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'sys': {'bg_png': '', 'bgm': (0, 0), 'env': (0, 0), 'map': 33, 'map_pos': (0.000, 0.000, 0.000), 'map_rot': (0.000, 0.000, 0.000), 'wav': ('', 0, 1)},
            'Me': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 0, 1), 'anim': (2, 9, 0), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.000, 'cloth_all': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 'cloth_type': 2, 'eyes': 0, 'eyes_blink': 0, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 0, 'face_to_full': (), 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 0, 'mouth_open': 0.000, 'move_to': (2.893, 8.440, 1.378), 'nip_stand': 0.000, 'rotate_to': (0.000, 36.046, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'trollnock': {'color': (((0.34, 0.37, 0.12, 1.00), (0.00, 0.00, 0.00, 1.00), 0.400, 0.369), ), 'fk_set': ((0.000, 0.000, 0.000), (45.023, 0.000, 0.000), (-40.469, 0.000, 0.000), (-5.066, 0.000, 0.000), (0.000, 0.000, 0.000), (0.000, 0.000, 0.000)), 'move_to': (-0.015, -0.185, -0.013), 'rotate_to': (332.574, 10.686, 359.976), 'scale_to': (1.300, 1.300, 1.300), 'visible': 1},
        }],
        #-VNFA:seq:end:1-#
    ], toSeq2)

def toSeq2(game):
    game.texts_next([
        #-VNFA:seq:start:2-#
        ["s", "", act, {
            'cam': {'goto_pos': ((-11.537, 9.101, 4.490), (0.000, 0.000, -6.699), (12.540, 166.001, 0.000))},
            'Kassandra': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (0, 0, 0), 'anim_lp': 1, 'anim_ptn': 0.000, 'anim_spd': 0.596, 'cloth_all': (0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0), 'cloth_type': 0, 'eyes': 9, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full': (4, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 63, 237, 125, 195, 189, 79, 170, 175, 61, 172, 68, 7, 60, 219, 223, 125, 63), 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {}, 'hands': (1, 1), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {'cf_J_ArmLow01_L': ((-0.154, 1.670, 0.193), ), 'cf_J_ArmLow01_R': ((0.234, 1.622, 0.115), ), 'cf_J_ArmUp00_L': ((-0.075, 1.469, -0.038), ), 'cf_J_ArmUp00_R': ((0.183, 1.468, 0.020), ), 'cf_J_Foot01_L': ((-0.191, 0.086, -0.041), (12.924, 3.762, 355.283)), 'cf_J_Foot01_R': ((0.169, 0.086, -0.031), (11.208, 353.872, 0.373)), 'cf_J_Hand_L': ((0.065, 1.869, 0.034), (3.240, 209.645, 294.548)), 'cf_J_Hand_R': ((0.067, 1.844, 0.005), (28.967, 197.607, 94.925)), 'cf_J_Hips': ((0.065, 1.120, 0.036), ), 'cf_J_LegLow01_L': ((-0.102, 0.541, 0.020), ), 'cf_J_LegLow01_R': ((0.151, 0.546, 0.055), ), 'cf_J_LegUp00_L': ((-0.032, 0.942, -0.016), ), 'cf_J_LegUp00_R': ((0.140, 0.944, 0.020), )}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 1, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 12, 'mouth_open': 0.779, 'move_to': (-10.605, 7.832, 2.355), 'nip_stand': 0.000, 'rotate_to': (0.000, 12.368, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'Bloodsplat': {'move_to': (-10.824, 10.367, 13.264), 'rotate_to': (0.000, 0.000, 0.000), 'visible': 1},
            'Troll': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (9, 167, 0), 'anim_lp': 0, 'anim_ptn': -1.000, 'anim_spd': 0.000, 'cloth_all': (0, 0), 'cloth_type': 0, 'eyes': 4, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_to': 4, 'face_to_full': (4, 0, 0, 0, 2, 0, 0, 0, 136, 32, 56, 61, 0, 0, 0, 50, 0, 0, 0, 0, 193, 189, 127, 63, 99, 177, 33, 62, 229, 238, 110, 190, 58, 105, 29, 61, 184, 110, 117, 63), 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {}, 'hands': (1, 20), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 3, 'mouth_open': 0.346, 'move_to': (-10.553, 7.868, 4.533), 'rotate_to': (0.000, 178.660, 0.000), 'scale_to': (1.201, 1.201, 1.201), 'simple': 0, 'simple_color': (0.00, 0.00, 1.00, 1.00), 'son': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'Zelda': {'acc_all': (1, 1, 1, 0, 1, 0, 1, 1, 0, 0), 'anim': (1, 3, 21), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.000, 'cloth_all': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 'cloth_type': 2, 'eyes': 2, 'eyes_blink': 1, 'eyes_open': 0.713, 'face_red': 0.000, 'face_to': 4, 'face_to_full': (4, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 63, 68, 91, 239, 189, 96, 83, 54, 62, 70, 132, 174, 60, 28, 17, 122, 63), 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {}, 'hands': (1, 1), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {'cf_J_ArmLow01_L': ((-0.098, 1.674, 0.054), ), 'cf_J_ArmLow01_R': ((0.187, 1.604, 0.113), ), 'cf_J_ArmUp00_L': ((-0.075, 1.469, -0.038), ), 'cf_J_ArmUp00_R': ((0.183, 1.468, 0.020), ), 'cf_J_Foot01_L': ((-0.191, 0.086, -0.041), (12.924, 3.762, 355.283)), 'cf_J_Foot01_R': ((0.169, 0.086, -0.031), (11.208, 353.872, 0.373)), 'cf_J_Hand_L': ((0.020, 1.869, 0.034), (3.240, 209.645, 294.548)), 'cf_J_Hand_R': ((0.085, 1.841, -0.004), (28.967, 197.607, 94.925)), 'cf_J_Hips': ((0.065, 1.120, 0.036), ), 'cf_J_LegLow01_L': ((-0.102, 0.541, 0.020), ), 'cf_J_LegLow01_R': ((0.153, 0.547, 0.058), ), 'cf_J_LegUp00_L': ((-0.032, 0.942, -0.016), ), 'cf_J_LegUp00_R': ((0.140, 0.944, 0.020), )}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 1, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 6, 'mouth_open': 0.426, 'move_to': (-11.810, 7.599, 2.345), 'nip_stand': 0.000, 'rotate_to': (0.000, 21.663, 0.000), 'scale_to': (1.100, 1.100, 1.100), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'sys': {'bg_png': '', 'bgm': (0, 0), 'env': (0, 0), 'map': 33, 'map_pos': (0.000, 0.000, 0.000), 'map_rot': (0.000, 0.000, 0.000), 'wav': ('', 0, 1)},
            'Me': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 0, 1), 'anim': (2, 9, 0), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.000, 'cloth_all': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 'cloth_type': 2, 'eyes': 0, 'eyes_blink': 0, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 0, 'face_to_full': (), 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 0, 'mouth_open': 0.000, 'move_to': (2.893, 8.440, 1.378), 'nip_stand': 0.000, 'rotate_to': (0.000, 36.046, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'trollnock': {'color': (((0.34, 0.37, 0.12, 1.00), (0.00, 0.00, 0.00, 1.00), 0.400, 0.369), ), 'fk_set': ((0.000, 0.000, 0.000), (45.023, 0.000, 0.000), (-40.469, 0.000, 0.000), (-5.066, 0.000, 0.000), (0.000, 0.000, 0.000), (0.000, 0.000, 0.000)), 'move_to': (-0.015, -0.185, -0.013), 'rotate_to': (332.574, 10.686, 359.976), 'scale_to': (1.300, 1.300, 1.300), 'visible': 1},
        }],
        ["s", "2", act, {
            'Ming': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (8, 142, 0), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.000, 'cloth_all': (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2), 'cloth_type': 1, 'eyes': 0, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 1, 'face_to_full': (), 'fk_active': (0, 0, 0, 1, 0, 0, 0), 'fk_set': {}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 1, 'mouth_open': 0.257, 'move_to': (-1.433, 0.017, 52.678), 'nip_stand': 0.000, 'rotate_to': (0.000, 327.688, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'cam': {'goto_pos': ((-2.310, 0.794, 53.621), (0.000, 0.000, -4.480), (10.650, -249.001, 0.000))},
            'Nia': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (8, 142, 0), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.000, 'cloth_all': (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2), 'cloth_type': 2, 'eyes': 0, 'eyes_blink': 0, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 1, 'face_to_full': (), 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 0, 'mouth_open': 0.000, 'move_to': (-0.733, 0.012, 53.401), 'nip_stand': 0.000, 'rotate_to': (0.000, 270.006, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'Jeanne': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (8, 142, 3), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 0.427, 'cloth_all': (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2), 'cloth_type': 1, 'eyes': 0, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 1, 'face_to_full': (), 'fk_active': (0, 1, 0, 0, 0, 0, 1), 'fk_set': {78: (-6.328, 0.000, 0.000), 79: (-6.559, 0.000, 0.000), 80: (-16.542, -44.704, -1.150), 81: (15.903, 0.000, -0.001), 82: (0.000, 0.000, 0.000), 83: (0.000, 0.000, 0.000), 84: (-39.393, 3.288, -19.671), 85: (8.413, 55.909, -11.000), 86: (0.295, 0.000, -4.987), 87: (0.000, 0.000, 0.000), 88: (0.000, 0.000, 0.000), 89: (0.000, 0.000, 0.000), 90: (-8.193, 2.724, -18.460), 91: (23.976, 0.000, 0.000), 92: (0.000, 0.000, 0.000), 93: (0.000, 0.000, 0.000), 94: (0.000, 0.000, 0.000), 95: (0.000, 0.000, 0.000), 96: (0.000, 0.000, 0.000), 97: (0.000, 0.000, 0.000), 98: (0.000, 0.000, 0.000), 99: (0.000, 0.000, 0.000), 100: (0.000, 0.000, 0.000), 101: (0.000, 0.000, 0.000), 102: (0.000, 0.000, 0.000), 103: (0.000, 0.000, 0.000), 104: (0.000, 0.000, 0.000), 105: (0.000, 0.000, 0.000), 106: (0.000, 0.000, 0.000), 107: (0.000, 0.000, 0.000), 108: (0.000, 0.000, 0.000), 109: (0.000, 0.000, 0.000), 110: (0.000, 0.000, 0.000), 111: (0.000, 0.000, 0.000), 112: (0.000, 0.000, 0.000), 113: (0.000, 0.000, 0.000), 114: (0.000, 0.000, 0.000), 115: (0.000, 0.000, 0.000), 116: (23.939, 0.000, 0.000), 117: (0.000, 0.000, 0.000), 118: (0.000, 0.000, 0.000), 119: (0.000, 0.000, 0.000), 120: (1.205, -2.929, 35.112), 121: (0.000, 0.000, 0.000), 122: (-18.341, -0.439, -41.993), 123: (0.000, 0.000, 0.000), 124: (0.000, 0.000, 0.000), 125: (0.000, 0.000, 0.000)}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 5, 'mouth_open': 0.000, 'move_to': (-2.217, -0.013, 52.787), 'nip_stand': 0.000, 'rotate_to': (0.000, 43.371, 0.000), 'scale_to': (0.900, 0.900, 0.900), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'Tanselle': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (8, 142, 3), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.000, 'cloth_all': (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2), 'cloth_type': 1, 'eyes': 0, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 1, 'face_to_full': (), 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 4, 'mouth_open': 0.588, 'move_to': (-1.241, -0.017, 54.058), 'nip_stand': 0.000, 'rotate_to': (0.000, 213.782, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'Lim': {'acc_all': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (8, 142, 3), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 1.000, 'cloth_all': (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2), 'cloth_type': 1, 'eyes': 0, 'eyes_blink': 1, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 1, 'face_to_full': (), 'fk_active': (0, 1, 0, 1, 0, 0, 0), 'fk_set': {}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 0, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 0, 'mouth': 1, 'mouth_open': 0.235, 'move_to': (-2.238, 0.003, 53.854), 'nip_stand': 0.000, 'rotate_to': (0.000, 146.589, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'sys': {'map': -1},
            'Me': {'acc_all': (0, 1, 1, 1, 1, 1, 0, 1, 1, 1), 'anim': (0, 1, 26), 'cloth_all': (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2), 'cloth_type': 0, 'face_to': 4, 'face_to_full': (4, 0, 0, 0, 2, 0, 0, 0, 254, 255, 255, 177, 172, 146, 66, 62, 254, 255, 127, 50, 12, 86, 123, 63, 170, 90, 232, 189, 132, 37, 161, 62, 255, 84, 27, 61, 88, 13, 113, 63), 'move_to': (-2.010, 0.031, 53.345), 'rotate_to': (0.000, 110.852, 0.000)},
        }],
        ["s", "3", act, {
            'Me': {'visible': 0},
            'cam': {'goto_pos': ((-1.798, 0.596, 53.355), (0.000, 0.000, 0.000), (-22.450, -36.901, 0.000))},
        }],
        #-VNFA:seq:end:2-#
    ], toSeq3)

def toSeq3(game):
    game.texts_next([
        #-VNFA:seq:empty:3-#
    ], toEnd)
    
#-VNFA:sel:empty:1-#
    
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
