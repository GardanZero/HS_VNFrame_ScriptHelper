#vngame;neo;Syl5TrainingRoom
# -*- coding: UTF-8 -*-
#-VNFA:BuildFromAutoScriptTemplate-#
# UTF-8 encode is supported now! ^o^

import random

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
    game.isHideWindowDuringCameraAnimation = False
    game.isLockWindowDuringSceneAnimation = False
    
    # load scene PNG and then init scene after loaded
    enableQuickReload = False
    game.sceneDir = "Syl\\"
    if enableQuickReload and hasattr(game, "scenePNG") and game.scenePNG == "Syl5TrainingRoom.png":
        # skip load png, quick reload
        # all actor/prop status must be reset by script
        init_scene(game)
    else:
        load_and_init_scene(game, "Syl5TrainingRoom.png", init_scene)
    
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
        choice_Training_Room(game)

    except Exception as e:
        import traceback
        traceback.print_exc()
        toEnd(game, "init_scene FAILED: "+str(e))

ringLevel = 1
experience = 0
sylvanasRep = 1
likaOrcRep = 0
shylethBFrep = 0
kareeshaOrcrep = 0
STR = 40
INT = 4
globvarLastChoice = "None"
lastPlayerAttack = "High"
lastPlayerDefense = "High"
fightHighHitSum = 0
fightMiddleHitSum = 0
fightLowHitSum = 0
HP_player_current = 4

# who's turn is it (player = 1, npc = 2, npc starts)
fight_who_turn = 2

def choice_Training_Room(game): 
    global STR
    global HP_player_current
    HP_player_float = (STR / 10)
    HP_player_current = round(HP_player_float,0)
    game.set_text("s", "What do you want to do? (Your HP: %d)" % (HP_player_current)) 
    game.set_buttons(["Challenge to a fight", "Train Strength/HP", "Go Back"], [choice_Fight_Defense, toEnd])

def choice_Fight_Defense(game): 
 	game.set_text("s", "Your opponent is attacking. How do you want to defend?") 
 	game.set_buttons(["High", "Medium", "Low"], [player_Defend_High, player_Defend_Medium, player_Defend_Low])

def choice_Fight_Attack(game): 
 	game.set_text("s", "How do you want to attack?") 
 	game.set_buttons(["High", "Medium", "Low"], [player_Attack_High, player_Attack_Medium, player_Attack_Low])

#Player Attack
def player_Attack_High(game):
 	global lastPlayerAttack
 	lastPlayerAttack = 1
 	game.set_text("s", "You attack high") 
 	game.set_buttons(["Next"], [check_Defense_NPC])

def player_Attack_Medium(game):
 	global lastPlayerAttack
 	lastPlayerAttack = 2
 	game.set_text("s", "You attack medium") 
 	game.set_buttons(["Next"], [check_Defense_NPC])

def player_Attack_Low(game):
 	global lastPlayerAttack
 	lastPlayerAttack = 3
 	game.set_text("s", "You attack low") 
 	game.set_buttons(["Next"], [check_Defense_NPC])

#Player Defense
def player_Defend_High(game):
 	global lastPlayerDefense
 	lastPlayerDefense = 1
 	game.set_text("s", "You defend high") 
 	game.set_buttons(["Next"], [check_Defense_Player])

def player_Defend_Medium(game):
 	global lastPlayerDefense
 	lastPlayerDefense = 2
 	game.set_text("s", "You defend medium") 
 	game.set_buttons(["Next"], [check_Defense_Player])

def player_Defend_Low(game):
 	global lastPlayerDefense
 	lastPlayerDefense = 3
 	game.set_text("s", "You defend low") 
 	game.set_buttons(["Next"], [check_Defense_Player])

#Scenes NPC Defense
def toSeqNPCDefenseLow(game):
        game.texts_next([
            ["s", "NPC parried low", act, {
            'Orc': {'acc_all': (1, 0, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (0, 1, 19, 0.000), 'anim_lp': 1, 'anim_ptn': 0.000, 'anim_spd': 0.000, 'cloth_all': (0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0), 'cloth_type': 0, 'eyes': 3, 'eyes_blink': 0, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAADAXF29ifpmvjrFDj3E23g/UWRavYOEab6r0hk8dd54Pw==', 'fk_active': (0, 1, 0, 1, 0, 0, 1), 'fk_set': {0: (12.000, -13.293, 8.494), 1: (-21.385, 27.066, -9.615), 2: (0.000, 20.000, 0.000), 3: (10.000, -10.000, -15.000), 4: (5.000, -10.000, -13.000), 5: (-10.511, 0.000, 0.000), 6: (-64.095, -69.654, 104.590), 7: (74.685, 0.000, 0.000), 8: (37.718, -31.789, -30.220), 9: (0.000, 0.000, 0.000), 10: (-41.317, -5.299, -26.804), 11: (28.012, -180.000, -180.000), 12: (11.367, 5.775, -2.552), 13: (-80.555, 168.934, 178.840), 14: (0.000, -15.000, 0.000), 15: (-57.899, -43.675, -39.883), 16: (0.000, -119.518, 0.000), 17: (-57.146, -49.594, 38.611), 18: (-10.000, -15.000, -12.000), 19: (-27.082, 55.102, -7.777), 20: (0.000, 138.509, 0.000), 21: (-8.435, -75.615, -41.259), 77: (0.000, 0.000, 0.000), 78: (0.000, 0.000, 0.000), 79: (0.000, 0.000, 0.000), 80: (0.000, 0.000, 0.000), 81: (0.000, 0.000, 0.000), 82: (0.000, 0.000, 0.000), 83: (0.000, 0.000, 0.000), 84: (0.000, 0.000, 0.000), 85: (0.000, 0.000, 0.000), 86: (0.000, 0.000, 0.000), 87: (0.000, 0.000, 0.000), 88: (0.000, 0.000, 0.000), 89: (0.000, 0.000, 0.000), 90: (0.000, 0.000, 0.000), 91: (0.000, 0.000, 0.000), 92: (0.000, 0.000, 0.000), 93: (0.000, 0.000, 0.000), 94: (0.000, 0.000, 0.000), 95: (0.000, 0.000, 0.000), 96: (0.000, 0.000, 0.000), 97: (0.000, 0.000, 0.000), 98: (0.000, 0.000, 0.000), 99: (0.000, 0.000, 0.000), 100: (0.000, 0.000, 0.000), 101: (0.000, 0.000, 0.000), 102: (0.000, 0.000, 0.000), 103: (0.000, 0.000, 0.000), 104: (0.000, 0.000, 0.000), 105: (0.000, 0.000, 0.000), 106: (0.000, 0.000, 0.000), 107: (0.000, 0.000, 0.000), 108: (0.000, 0.000, 0.000), 109: (0.000, 0.000, 0.000), 110: (0.000, 0.000, 0.000), 111: (0.000, 0.000, 0.000), 112: (0.000, 0.000, 0.000), 113: (0.000, 0.000, 0.000), 114: (0.000, 0.000, 0.000), 115: (0.000, 0.000, 0.000), 116: (0.000, 0.000, 0.000), 117: (0.000, 0.000, 0.000), 118: (0.000, 0.000, 0.000), 119: (0.000, 0.000, 0.000), 120: (0.000, 0.000, 0.000), 121: (0.000, 0.000, 0.000), 122: (0.000, 0.000, 0.000), 123: (0.000, 0.000, 0.000), 124: (0.000, 0.000, 0.000)}, 'hands': (0, 1), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 2, 'lip_sync': 1, 'look_at_pos': (-0.034, 0.304, 0.209), 'look_at_ptn': 4, 'mouth': 1, 'mouth_open': 0.566, 'move_to': (-25.055, 3.385, 10.429), 'nip_stand': 0.000, 'rotate_to': (0.000, 65.110, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.338, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'cam': {'goto_pos': ((-24.962, 4.033, 10.645), (0.000, 0.000, -2.413), (9.300, -58.551, 0.000))},
            'oldSword': {'fk_set': ((0.000, 0.000, 0.000), ), 'move_to': (-5.953, -0.190, 0.023), 'rotate_to': (336.541, 162.602, 349.682), 'scale_to': (0.700, 0.700, 0.700), 'visible': 1},
            'sys': {'bg_png': '', 'bgm': (0, 0), 'char_light': ((0.86, 0.82, 0.80, 1.00), 0.623, 74.000, 330.000, 1), 'env': (0, 0), 'map': -1, 'map_pos': (0.000, 0.000, 0.000), 'map_rot': (0.000, 0.000, 0.000), 'wav': ('', 0, 1)},
        }],
    ], choice_Fight_Defense)


def toSeqNPCDefenseMedium(game):
        game.texts_next([
            ["s", "npc parry medium", act, {
                'Orc': {'acc_all': (1, 0, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (0, 2, 11, 0.000), 'anim_lp': 1, 'anim_ptn': 0.000, 'anim_spd': 0.000, 'cloth_all': (0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0), 'cloth_type': 0, 'eyes': 3, 'eyes_blink': 0, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAADAXF29ifpmvjrFDj3E23g/UWRavYOEab6r0hk8dd54Pw==', 'fk_active': (0, 1, 0, 1, 1, 1, 1), 'fk_set': {0: (3.135, 10.689, -7.945), 1: (27.930, -31.565, -3.292), 2: (-6.046, -31.312, 0.000), 3: (-12.321, 0.693, 4.212), 4: (-0.491, -6.168, 8.664), 5: (0.000, 2.671, 0.000), 6: (-4.471, -0.099, 3.708), 7: (24.281, 0.000, 0.000), 8: (-14.787, 10.805, 0.869), 9: (-10.879, 0.000, 0.000), 10: (1.668, -23.531, 11.131), 11: (-1.537, 0.000, 0.000), 12: (0.000, 0.000, 0.000), 13: (0.000, 0.000, 0.000), 14: (5.894, -11.554, 37.098), 15: (-43.796, -120.192, 52.823), 16: (0.000, -101.623, 0.000), 17: (48.556, 21.248, 68.012), 18: (-0.555, 8.162, -5.087), 19: (-74.860, -172.346, -128.879), 20: (0.000, 100.808, 0.000), 21: (34.977, -1.453, -29.548), 22: (6.012, -5.598, -32.017), 23: (18.448, -0.590, 1.781), 24: (0.000, 14.441, 0.000), 25: (7.325, -7.024, -43.185), 26: (0.000, 0.000, -76.533), 27: (0.000, 0.000, -50.319), 28: (0.000, 0.000, -49.704), 29: (0.000, 0.000, -76.974), 30: (0.000, 0.000, -71.575), 31: (-9.730, 10.038, -38.831), 32: (0.000, 0.000, -75.236), 33: (0.000, 0.000, -75.254), 34: (-18.223, 20.247, -28.002), 35: (0.000, 0.000, -56.723), 36: (0.000, 0.000, -70.356), 37: (1.644, 6.100, 6.058), 38: (0.000, 18.413, 0.000), 39: (0.000, -12.351, 0.000), 40: (0.000, 0.898, -10.594), 41: (-1.926, 0.000, 28.002), 42: (0.000, 0.000, 21.275), 43: (4.882, 0.000, 3.786), 44: (0.000, 0.000, 50.072), 45: (0.000, 0.000, 24.787), 46: (-8.341, 0.358, 9.578), 47: (0.000, 0.000, 40.327), 48: (0.000, 0.000, 37.869), 49: (-19.711, 0.000, 21.780), 50: (0.000, 0.000, 48.523), 51: (0.000, -3.345, 52.081), 77: (0.000, 0.000, 0.000), 78: (0.000, 0.000, 0.000), 79: (6.875, 0.000, 0.000), 80: (0.000, 0.000, 0.000), 81: (0.000, 0.000, 0.000), 82: (0.000, 0.000, 0.000), 83: (0.000, 0.000, 0.000), 84: (0.000, 0.000, 0.000), 85: (0.000, 0.000, 0.000), 86: (0.000, 0.000, 0.000), 87: (0.000, 0.000, 0.000), 88: (0.000, 0.000, 0.000), 89: (0.000, 0.000, 0.000), 90: (0.000, 0.000, 0.000), 91: (0.000, 0.000, 0.000), 92: (0.000, 0.000, 0.000), 93: (0.000, 0.000, 0.000), 94: (0.000, 0.000, 0.000), 95: (0.000, 0.000, 0.000), 96: (0.000, 0.000, 0.000), 97: (0.000, 0.000, 0.000), 98: (0.000, 0.000, 0.000), 99: (0.000, 0.000, 0.000), 100: (0.000, 0.000, 0.000), 101: (0.000, 0.000, 0.000), 102: (0.000, 0.000, 0.000), 103: (0.000, 0.000, 0.000), 104: (0.000, 0.000, 0.000), 105: (0.000, 0.000, 0.000), 106: (0.000, 0.000, 0.000), 107: (0.000, 0.000, 0.000), 108: (-12.963, -1.109, -18.362), 109: (-20.215, 14.458, -36.728), 110: (-3.236, 0.000, 0.000), 111: (0.000, 0.000, 0.000), 112: (0.000, 0.000, 0.000), 113: (0.000, 0.000, 0.000), 114: (0.000, 0.000, 0.000), 115: (6.227, 10.005, 58.416), 116: (0.000, 0.000, 0.000), 117: (0.000, 0.000, 0.000), 118: (0.000, 0.000, 0.000), 119: (0.000, 0.000, 0.000), 120: (0.000, 0.000, 38.919), 121: (0.000, 0.000, 0.000), 122: (0.000, 0.000, 0.000), 123: (0.000, 0.000, 0.000), 124: (0.000, 0.000, 0.000)}, 'hands': (0, 1), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 2, 'lip_sync': 1, 'look_at_pos': (-0.022, -0.266, 0.533), 'look_at_ptn': 4, 'mouth': 1, 'mouth_open': 0.566, 'move_to': (-25.055, 3.385, 10.429), 'nip_stand': 0.000, 'rotate_to': (0.000, 159.969, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.338, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
                'cam': {'goto_pos': ((-24.571, 4.516, 10.500), (0.000, 0.000, -2.864), (-6.900, -116.400, 0.000))},
                'oldSword': {'fk_set': ((0.000, 0.000, 0.000), ), 'move_to': (-6.133, 0.257, -0.073), 'rotate_to': (311.413, 349.040, 158.257), 'scale_to': (0.700, 0.700, 0.700), 'visible': 1},
                'sys': {'bg_png': '', 'bgm': (0, 0), 'char_light': ((0.86, 0.82, 0.80, 1.00), 0.623, 74.000, 330.000, 1), 'env': (0, 0), 'map': -1, 'map_pos': (0.000, 0.000, 0.000), 'map_rot': (0.000, 0.000, 0.000), 'wav': ('', 0, 1)},
            }],
    ], choice_Fight_Defense)

def toSeqNPCDefenseHigh(game):
        game.texts_next([
        ["s", "npcdefendhigh", act, {
            'Orc': {'acc_all': (1, 0, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (0, 2, 11, 0.000), 'anim_lp': 1, 'anim_ptn': 0.000, 'anim_spd': 0.000, 'cloth_all': (0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0), 'cloth_type': 0, 'eyes': 3, 'eyes_blink': 0, 'eyes_open': 1.000, 'face_red': 0.000, 'face_to': 4, 'face_to_full2': 'BAAAAAIAAADAXF29ifpmvjrFDj3E23g/UWRavYOEab6r0hk8dd54Pw==', 'fk_active': (1, 1, 0, 1, 1, 1, 1), 'fk_set': {1: (6.294, -13.841, 15.763), 2: (-0.734, -26.082, 0.621), 9: (0.000, 0.000, 0.000), 13: (0.000, 0.000, 0.000), 22: (38.319, -17.030, -40.312), 23: (-4.485, -26.907, 5.419), 24: (0.000, 33.036, 0.000), 25: (6.766, -3.874, -79.761), 26: (0.000, 0.000, -72.859), 27: (0.000, 0.000, -76.912), 28: (1.303, 0.607, -81.510), 29: (0.000, 0.000, -72.859), 30: (0.000, 0.000, -87.169), 31: (-4.081, 6.826, -76.888), 32: (0.000, 0.000, -72.859), 33: (0.000, 0.000, -76.818), 34: (-12.501, 10.255, -76.037), 35: (0.000, 0.000, -72.909), 36: (0.000, 0.000, -68.097), 37: (-0.768, 9.134, 5.549), 38: (0.000, 26.586, 0.000), 39: (0.000, 10.734, 0.000), 40: (-1.304, 3.215, 5.526), 41: (0.000, 0.000, 23.560), 42: (0.000, 0.000, 21.540), 43: (0.354, -1.336, 17.322), 44: (0.000, 0.000, 26.072), 45: (0.000, 0.000, 22.694), 46: (-0.096, -6.340, 23.147), 47: (0.000, 0.000, 24.665), 48: (0.000, 0.000, 26.963), 49: (-1.763, -10.619, 22.992), 50: (0.000, 0.000, 24.283), 51: (0.000, 0.000, 28.331), 52: (0.000, 0.000, 0.000), 53: (0.000, 0.000, 0.000), 54: (0.000, 0.000, 0.000), 55: (0.000, 0.000, 6.361), 56: (0.000, 0.000, 4.690), 57: (0.000, 0.000, 67.561), 58: (0.000, 0.000, 0.000), 59: (0.000, 0.000, 0.000), 60: (0.000, 0.000, 0.000), 61: (0.000, 0.000, 52.202), 62: (0.000, 0.000, 38.345), 63: (-31.698, 0.000, 0.000), 64: (0.000, 0.000, 0.000), 77: (0.000, 0.000, 0.000), 78: (0.000, 0.000, 0.000), 79: (6.875, 0.000, 0.000), 80: (0.000, 0.000, 0.000), 81: (0.000, 0.000, 0.000), 82: (0.000, -12.433, 0.000), 83: (0.000, 0.000, 0.000), 84: (-28.850, 0.000, 0.000), 85: (0.000, 0.000, 0.000), 86: (0.000, 0.000, 0.000), 87: (0.000, 0.000, 0.000), 88: (0.000, 0.000, 0.000), 89: (0.000, 0.000, 0.000), 90: (-21.422, 0.000, 0.000), 91: (0.000, 0.000, 0.000), 92: (0.000, 0.000, 0.000), 93: (0.000, 0.000, 0.000), 94: (0.000, 0.000, 0.000), 95: (31.896, 0.851, 3.994), 96: (0.000, 0.000, 0.000), 97: (0.000, 0.000, 0.000), 98: (0.000, 0.000, 0.000), 99: (0.000, 0.000, 0.000), 100: (0.000, 0.000, 0.000), 101: (0.000, 0.000, 0.000), 102: (0.000, 0.000, 0.000), 103: (0.000, 0.000, 0.000), 104: (0.000, 0.000, 0.000), 105: (0.000, 0.000, 0.000), 106: (0.000, 0.000, 0.000), 107: (0.000, 0.000, 0.000), 108: (-12.963, -1.109, -18.362), 109: (-20.215, 14.458, -36.728), 110: (-3.236, 0.000, 0.000), 111: (13.859, 0.000, 0.000), 112: (0.000, 0.000, 0.000), 113: (0.000, 0.000, 0.000), 114: (-33.470, 0.047, -0.218), 115: (25.835, 17.618, 21.651), 116: (0.000, 0.000, 5.129), 117: (0.000, 0.000, 0.000), 118: (0.000, 0.000, 0.000), 119: (0.000, 0.000, 0.000), 120: (-10.109, -8.277, 39.653), 121: (0.000, 0.000, 0.000), 122: (0.000, 0.000, 0.000), 123: (0.000, 0.000, 0.000), 124: (0.000, 0.000, 0.000)}, 'hands': (0, 1), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {'cf_J_ArmLow01_L': ((0.230, 1.306, 0.237), ), 'cf_J_ArmLow01_R': ((0.187, 1.513, -0.202), ), 'cf_J_ArmUp00_L': ((0.020, 1.363, 0.217), ), 'cf_J_ArmUp00_R': ((0.040, 1.461, 0.000), ), 'cf_J_Foot01_L': ((-0.110, 0.277, 0.560), (0.752, 50.858, 345.462)), 'cf_J_Foot01_R': ((0.030, 0.266, -0.497), (359.836, 80.101, 10.551)), 'cf_J_Hand_L': ((0.365, 1.466, 0.185), (27.127, 216.505, 264.375)), 'cf_J_Hand_R': ((0.452, 1.581, 0.165), (21.097, 287.686, 41.303)), 'cf_J_Hips': ((0.000, 1.101, 0.000), ), 'cf_J_LegLow01_L': ((0.040, 0.646, 0.349), ), 'cf_J_LegLow01_R': ((0.187, 0.637, -0.294), ), 'cf_J_LegUp00_L': ((-0.004, 0.939, 0.074), ), 'cf_J_LegUp00_R': ((0.035, 0.952, -0.090), )}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 3, 'lip_sync': 1, 'look_at_pos': (-0.074, -0.061, 0.430), 'look_at_ptn': 4, 'mouth': 1, 'mouth_open': 0.566, 'move_to': (-25.055, 3.385, 10.429), 'nip_stand': 0.000, 'rotate_to': (0.000, 55.462, 0.000), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.338, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
            'cam': {'goto_pos': ((-24.805, 4.518, 10.319), (0.000, 0.000, -3.454), (-16.000, -65.200, 0.000))},
            'oldSword': {'fk_set': ((0.000, 0.000, 0.000), ), 'move_to': (-6.060, 0.459, -0.003), 'rotate_to': (288.927, 95.539, 86.601), 'scale_to': (0.700, 0.700, 0.700), 'visible': 1},
            'sys': {'bg_png': '', 'bgm': (0, 0), 'char_light': ((0.86, 0.82, 0.80, 1.00), 0.623, 74.000, 330.000, 1), 'env': (0, 0), 'map': -1, 'map_pos': (0.000, 0.000, 0.000), 'map_rot': (0.000, 0.000, 0.000), 'wav': ('', 0, 1)},
        }],
    ], choice_Fight_Defense)

        
#Check defense NPC        
def check_Defense_NPC(game):
    global lastPlayerAttack
    global fightHighHitSum
    
    rndTest = random.randint(1, 3)
      
    #Has NPC parried High
    if rndTest == lastPlayerAttack and lastPlayerAttack == 1:
        toSeqNPCDefenseHigh(game)
    #Has NPC parried Middle
    if rndTest == lastPlayerAttack and lastPlayerAttack == 2:
        toSeqNPCDefenseMedium(game)
    #Has NPC parried Low
    if rndTest == lastPlayerAttack and lastPlayerAttack == 3:
        toSeqNPCDefenseLow(game)
    # Check if player has hit and add up
    if rndTest != lastPlayerAttack:
        fightHighHitSum = fightHighHitSum+1
        #TODO
        toSeqNPCDefenseLow(game)
        
#    else:
#        game.set_text("s", "You score a hit! (%d hits total)" % (fightHighHitSum))
#        
#    if fightHighHitSum > 6:
#        game.set_buttons(["Many hits next"], [toSeqDefeatNPC])
#    else:
#        game.set_buttons(["Not enough hits next"], [choice_Fight_Defense])

#Check defense player
def check_Defense_Player(game):
    global lastPlayerAttack
    global HP_player_current
    
    rndTest = random.randint(1, 3)
    
    # Check if player has hit and add up
    if rndTest == lastPlayerAttack:
        game.set_text("s", "You parry the blow! %d" % (rndTest))
        
    else:
        HP_player_current = HP_player_current -1
        game.set_text("s", "You get hit! (%d HP left)" % (HP_player_current))
        
    if HP_player_current < 1:
        game.set_buttons(["Player loose"], [toSeqDefeatPlayer])
    else:
        game.set_buttons(["HP left continue"], [choice_Fight_Attack])

def toSeqDefeatNPC(game):
    game.texts_next([
        #-VNFA:seq:start:2-#
        ["s", "You win!", act, {
            'Boy': {'acc_all': (0, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (3, 32, 1), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 0.198, 'cloth_all': (0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 2), 'cloth_type': 0, 'eyes': 12, 'eyes_blink': 0, 'eyes_open': 0.000, 'face_red': 0.176, 'face_to': 4, 'face_to_full': (4, 0, 0, 0, 2, 0, 0, 0, 93, 179, 1, 60, 0, 0, 0, 0, 0, 0, 0, 0, 242, 253, 127, 63, 182, 227, 159, 61, 114, 107, 178, 188, 165, 155, 223, 58, 72, 40, 127, 63), 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (-36.564, -13.202, 7.827), 2: (-13.306, -10.023, 6.447)}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {'cf_J_ArmLow01_L': ((-0.176, 0.031, -0.191), ), 'cf_J_ArmLow01_R': ((0.172, 0.030, -0.197), ), 'cf_J_ArmUp00_L': ((-0.106, 0.055, -0.386), ), 'cf_J_ArmUp00_R': ((0.099, 0.058, -0.401), ), 'cf_J_Foot01_L': ((-0.235, -0.015, 0.663), (357.139, 5.296, 356.116)), 'cf_J_Foot01_R': ((0.205, 0.001, 0.636), (358.051, 357.081, 5.060)), 'cf_J_Hand_L': ((-0.138, 0.041, 0.002), (326.511, 80.052, 7.758)), 'cf_J_Hand_R': ((0.150, 0.035, 0.006), (319.875, 294.876, 350.554)), 'cf_J_Hips': ((-0.025, 0.042, -0.127), ), 'cf_J_LegLow01_L': ((-0.146, 0.327, 0.306), ), 'cf_J_LegLow01_R': ((0.140, 0.330, 0.300), ), 'cf_J_LegUp00_L': ((-0.079, 0.097, 0.003), ), 'cf_J_LegUp00_R': ((0.066, 0.098, 0.000), )}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 3, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 10, 'mouth_open': 0.647, 'move_to': (14.928, 0.181, 4.801), 'nip_stand': 0.000, 'rotate_to': (1.699, 180.842, 359.278), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
        }],
        #-VNFA:seq:end:1-#
    ], choice_Fight_Attack)

def toSeqDefeatPlayer(game):
    game.texts_next([
        #-VNFA:seq:start:2-#
        ["s", "You lose!", act, {
            'Boy': {'acc_all': (0, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'anim': (3, 32, 1), 'anim_lp': 0, 'anim_ptn': 0.000, 'anim_spd': 0.198, 'cloth_all': (0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 2), 'cloth_type': 0, 'eyes': 12, 'eyes_blink': 0, 'eyes_open': 0.000, 'face_red': 0.176, 'face_to': 4, 'face_to_full': (4, 0, 0, 0, 2, 0, 0, 0, 93, 179, 1, 60, 0, 0, 0, 0, 0, 0, 0, 0, 242, 253, 127, 63, 182, 227, 159, 61, 114, 107, 178, 188, 165, 155, 223, 58, 72, 40, 127, 63), 'fk_active': (0, 1, 0, 0, 0, 0, 0), 'fk_set': {1: (-36.564, -13.202, 7.827), 2: (-13.306, -10.023, 6.447)}, 'hands': (0, 0), 'ik_active': (1, 1, 1, 1, 1), 'ik_set': {'cf_J_ArmLow01_L': ((-0.176, 0.031, -0.191), ), 'cf_J_ArmLow01_R': ((0.172, 0.030, -0.197), ), 'cf_J_ArmUp00_L': ((-0.106, 0.055, -0.386), ), 'cf_J_ArmUp00_R': ((0.099, 0.058, -0.401), ), 'cf_J_Foot01_L': ((-0.235, -0.015, 0.663), (357.139, 5.296, 356.116)), 'cf_J_Foot01_R': ((0.205, 0.001, 0.636), (358.051, 357.081, 5.060)), 'cf_J_Hand_L': ((-0.138, 0.041, 0.002), (326.511, 80.052, 7.758)), 'cf_J_Hand_R': ((0.150, 0.035, 0.006), (319.875, 294.876, 350.554)), 'cf_J_Hips': ((-0.025, 0.042, -0.127), ), 'cf_J_LegLow01_L': ((-0.146, 0.327, 0.306), ), 'cf_J_LegLow01_R': ((0.140, 0.330, 0.300), ), 'cf_J_LegUp00_L': ((-0.079, 0.097, 0.003), ), 'cf_J_LegUp00_R': ((0.066, 0.098, 0.000), )}, 'juice': (0, 0, 0, 0, 0), 'kinematic': 3, 'lip_sync': 1, 'look_at_pos': (0.000, 0.000, 0.250), 'look_at_ptn': 3, 'mouth': 10, 'mouth_open': 0.647, 'move_to': (14.928, 0.181, 4.801), 'nip_stand': 0.000, 'rotate_to': (1.699, 180.842, 359.278), 'scale_to': (1.000, 1.000, 1.000), 'skin_tuya': 0.000, 'tear': 0, 'visible': 1, 'voice_lst': (), 'voice_rpt': 0},
        }],
        #-VNFA:seq:end:1-#
    ], choice_Fight_Attack)
        
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
