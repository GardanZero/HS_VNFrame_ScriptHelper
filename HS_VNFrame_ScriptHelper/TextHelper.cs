using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HS_VNFrame_ScriptHelper
{
    public static class TextHelper
    {
        internal static string GetJumpToText(string currentString)
        {

            // find the jump to location
            int lastIndexOfBracket = currentString.LastIndexOf(")");
            int lastIndexOfSpace = currentString.LastIndexOf(" ");
            string jumpToLocation = "";

            try
            {

                if (lastIndexOfBracket - lastIndexOfSpace < 0)
                {
                    int lastIndexOfComma = currentString.LastIndexOf(", ");
                    jumpToLocation = currentString.Substring(lastIndexOfComma + 2, lastIndexOfBracket - lastIndexOfComma - 2);
                }
                else
                {
                    jumpToLocation = currentString.Substring(lastIndexOfSpace, lastIndexOfBracket - lastIndexOfSpace);
                }

                if (jumpToLocation.Contains("str(e)"))
                {
                    //look for "toSeq" use that
                    if (currentString.Contains("toSeq"))
                    {
                        int startIndex = currentString.IndexOf("toSeq");
                        string restString = currentString.Substring(startIndex);
                        int stopIndex = restString.IndexOf(")") + 1;
                        jumpToLocation = restString.Substring(0, stopIndex);
                    }
                    else if (jumpToLocation == "")
                    {
                        int startIndex = currentString.IndexOf("toEnd");
                        string restString = currentString.Substring(startIndex);
                        int stopIndex = restString.IndexOf(")") + 1;
                        jumpToLocation = restString.Substring(0, stopIndex);
                    }
                    else if (jumpToLocation == "clearExit(game")
                    {
                        jumpToLocation = jumpToLocation + ")";
                    }
                    else
                    {
                        // give up
                    }

                }
                if (jumpToLocation.Contains("]"))
                {/*
                    def toSeq0(game):    
                    game.set_text("Boy", "What should I do?")
                    game.set_buttons(["Start from beginning", "Go to part 2"], [toSeq1, toSc2_0])
                    */
                    int lastIndexOfOpenBracket = currentString.LastIndexOf("(");
                    jumpToLocation = currentString.Substring(lastIndexOfOpenBracket, lastIndexOfBracket - lastIndexOfOpenBracket);
     
                }
                else
                {
                    // give up
                }


            }
            catch
            {

            }

            return jumpToLocation;
        }

        public static Dictionary<string, string> ParseTextIntoDictionary(string[] splittedTextIntoDefs)
        {
            Dictionary<string, string> DetailsDictionary = new Dictionary<string, string>();

            string currentString = "";
            int treeIndex = 0;
            int subTreeIndex = 0;


            foreach (string splittedStringDef in splittedTextIntoDefs)
            {
                if (!splittedStringDef.StartsWith("#"))
                {
                    subTreeIndex = 1;

                    currentString = "def " + splittedStringDef;

                    // get name of def from string
                    string defName = "";

                    if (currentString.Contains(":"))
                    {
                        defName = currentString.Substring(0, currentString.IndexOf(":"));
                    }
                    else if (currentString.Length > 30)
                    {
                        defName = currentString.Substring(0, 29);

                    }
                    else
                    {
                        defName = currentString;
                    }

                    // add the jump To scene to the def name
                    string jumpPrefix = "       ------>      ";
                    string jumpToLocation = TextHelper.GetJumpToText(currentString);
                    defName = defName + jumpPrefix + jumpToLocation;



                    // Add node to Tree
                    treeIndex++;

                    DetailsDictionary.Add(treeIndex.ToString() + ".0", currentString);

                    // create Subnodes
                    string[] cameraString = new string[1];
                    cameraString[0] = "[\"";
                    string[] cameraSplit = currentString.Split(cameraString, StringSplitOptions.None);

                    foreach (string camera in cameraSplit)
                    {
                        string cameraSettings, cameraSettingsNodeName;
                        CreateNodeName(camera, out cameraSettings, out cameraSettingsNodeName);


                        DetailsDictionary.Add(treeIndex.ToString() + "." + subTreeIndex.ToString(), cameraSettings);
                        subTreeIndex++;
                    }
                }
                else
                {
                    // add the text at the beginning of the file as the first node

                    DetailsDictionary.Add("0.0", splittedStringDef);
                }
            }

            return DetailsDictionary;
        }

        public static void CreateNodeName(string camera, out string cameraSettings, out string cameraSettingsNodeName)
        {
            cameraSettings = "";
            if (!camera.StartsWith("def"))
            {
                cameraSettings = "[\"" + camera;
            }
            else
            {
                cameraSettings = camera;
            }

            cameraSettingsNodeName = "";
            if (cameraSettings.Contains('\r'))
            {
                cameraSettingsNodeName = cameraSettings.Substring(0, cameraSettings.IndexOf('\r'));
            }
            else
            {
                if (cameraSettings.Length > 49)
                {
                    cameraSettingsNodeName = cameraSettings.Substring(0, 50);
                }
                else
                {
                    cameraSettingsNodeName = cameraSettings.Substring(0, cameraSettings.Length);
                }
            }
        }
    }
}