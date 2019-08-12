using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace HS_VNFrame_ScriptHelper
{
    public class StructureLoader
    {
        public string Filename { get; set; }
        public TreeView StructureTreeView { get; set; }
        public string[] SplittedTextIntoDefs { get; set; }
        public TextBox RawViewTB { get; set; }
        public Dictionary<string, string> DetailsDictionary { get; set; }
        public LoaderForm LoaderForm { get; set; }
        public string LastNodeNumber { get; set; }
        public string LastNodeText { get; set; }
        public string LastNodeSpeaker { get; set; }
        public TreeNode LastNode { get; set; }

        public StructureLoader(string filename, LoaderForm loaderForm)
        {
            Filename = filename;
            StructureTreeView = loaderForm.structureTreeView;
            RawViewTB = loaderForm.RawViewTB;
            DetailsDictionary = new Dictionary<string, string>();
            LoaderForm = loaderForm;

        }

        public void LoadStructure()
        {
            // Read whole file
            string wholePyText = "";
            try
            {
                wholePyText = File.ReadAllText(Filename);
            }
            catch (Exception e)
            {
                MessageBox.Show("Something went wrong loading the file.");
            }

            StructureTreeView.Nodes.Clear();

            // Break text into sections for each def
            string[] defString = new string[1];
            defString[0] = "def ";
            SplittedTextIntoDefs = wholePyText.Split(defString, StringSplitOptions.None);
            string currentString = "";
            int treeIndex = 0;
            int subTreeIndex = 0;


            // Add Event handler
            StructureTreeView.NodeMouseClick += StructureTreeView_NodeMouseClick;

            foreach (string splittedStringDef in SplittedTextIntoDefs)
            {
                if (!splittedStringDef.StartsWith("#"))
                {
                    subTreeIndex = 0;

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

					// find the jump to location
					int lastIndexOfBracket = currentString.LastIndexOf(")");
					int lastIndexOfSpace = currentString.LastIndexOf(" ");
					string jumpToLocation = "";
					try
					{ 
						jumpToLocation = currentString.Substring(lastIndexOfSpace, lastIndexOfBracket-lastIndexOfSpace);
					}
					catch
					{

					}

					defName = defName + jumpPrefix + jumpToLocation;

					treeIndex++;
                    TreeNode newNode = StructureTreeView.Nodes.Add(treeIndex.ToString(), defName);

                    DetailsDictionary.Add(treeIndex.ToString(), currentString);

                    // create subnodes
                    string[] cameraString = new string[1];
                    cameraString[0] = "[\"";
                    string[] cameraSplit = currentString.Split(cameraString, StringSplitOptions.None);

                    foreach (string camera in cameraSplit)
                    {
                        string cameraSettings = "[\"" + camera;
                        string cameraSettingsNodeName = "";

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

                        TreeNode camChildNode = newNode.Nodes.Add(treeIndex.ToString() + "." + subTreeIndex.ToString(), cameraSettingsNodeName);
                        DetailsDictionary.Add(treeIndex.ToString() + "." + subTreeIndex.ToString(), cameraSettings);
                        subTreeIndex++;

                    }


                }
                else
                {
                    // add the text at the beginning of the file as the first node
                    TreeNode newNode = StructureTreeView.Nodes.Add("0", "vngame");
                    DetailsDictionary.Add("0", splittedStringDef);
                }


            }
        }

        private void LeftMouseButton_ShowDetails(object sender, TreeNodeMouseClickEventArgs e)
        {
           
                // which node was clicked?
                string nodeNumber = e.Node.Name;
                LastNodeNumber = nodeNumber;
                string nodeText = e.Node.Text;

                // get raw subtext of Node
                string rawNodeText = "";
                try
                {
                    rawNodeText = DetailsDictionary[nodeNumber];
                    RawViewTB.Text = rawNodeText;
                }
                catch (Exception)
                {

                }

                if (rawNodeText != "")
                {

                    // check if this is a subnode text
                    bool isProbablySubNodeText = true;
                    if (!nodeNumber.Contains(".")) { isProbablySubNodeText = false; }
                    if (rawNodeText.Contains("[\"def")) { isProbablySubNodeText = false; }

                    // if this is a sub node (a text with camera), we get some details
                    if (isProbablySubNodeText)
                    {
                        try
                        {
                            string[] speakerSeparator = new string[1];
                            speakerSeparator[0] = "\",";
                            string[] speakerTextSplit = rawNodeText.Split(speakerSeparator, StringSplitOptions.None);

                            string speaker = speakerTextSplit[0];
                            LoaderForm.speakerTB.Text = speaker.Substring(speaker.IndexOf("\"") + 1);
                            LastNodeSpeaker = speaker.Substring(speaker.IndexOf("\"") + 1);

                            string text = speakerTextSplit[1];
                            LoaderForm.textTB.Text = text.Substring(speaker.IndexOf("\"") + 1);
                            LastNodeText = text.Substring(speaker.IndexOf("\"") + 1);

                            LastNode = e.Node;
                        }
                        catch (Exception ex)
                        {
                            MessageBox.Show("Cannot extract reader and text. Probably this not a text node. " + ex.Message);
                        }
                    }
                    else
                    {
                        // this is not a camera node, but something else
                        if (rawNodeText.Contains("game.sceneDir ="))
                        {
                            // this node contains the game.sceneDir and (probably) the png file
                            //  game.sceneDir = "\\"
                            //  load_and_init_scene(game, "pool1.png", init_scene)
                            //  game.scenePNG == "pool1.png": 

                            string sceneDirPart = rawNodeText.Substring(rawNodeText.IndexOf("game.sceneDir"));
                            string sceneDirLine = sceneDirPart.Substring(sceneDirPart.IndexOf("\""));
                            string sceneDir = sceneDirLine.Substring(1, sceneDirLine.IndexOf("\r") - 2);
                            LoaderForm.sceneDirTB.Text = sceneDir;

                        }

                    }
                }
            
        }

        private void StructureTreeView_NodeMouseClick(object sender, TreeNodeMouseClickEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                LeftMouseButton_ShowDetails(sender, e);
            }
            if (e.Button == MouseButtons.Right)
            {
                // show a context menu
                // Select this node.
                TreeNode node_here = StructureTreeView.GetNodeAt(e.X, e.Y);
                StructureTreeView.SelectedNode = node_here;

                // See if we got a node.
                if (node_here == null)
                {
                    MessageBox.Show("No node found here, where we clicked. Error?");
                    return;
                }

                LoaderForm.contextMenuStrip1.Items.Clear();
                ToolStripItem insertBeforeItem = LoaderForm.contextMenuStrip1.Items.Add("Insert Node before");
                ToolStripItem deleteItem = LoaderForm.contextMenuStrip1.Items.Add("Delete Node");

                insertBeforeItem.Click += InsertBeforeItem_Click;
                deleteItem.Click += DeleteItem_Click;

                int showX = LoaderForm.Location.X + StructureTreeView.Location.X + StructureTreeView.SelectedNode.Bounds.Location.X +40;
                int showY = LoaderForm.Location.Y + StructureTreeView.Location.Y + StructureTreeView.SelectedNode.Bounds.Location.Y +60;
                
                LoaderForm.contextMenuStrip1.Show(new Point(showX,showY));
            }

        }

        private void DeleteItem_Click(object sender, EventArgs e)
        {
            // TODO get which node got clicked
            // Delete item from dictionary
            // rebuild structure

            throw new NotImplementedException();
        }

        private void InsertBeforeItem_Click(object sender, EventArgs e)
        {
            int i = 1;
            throw new NotImplementedException();
        }
    }
}