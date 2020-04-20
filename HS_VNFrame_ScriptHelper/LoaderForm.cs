using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace HS_VNFrame_ScriptHelper
{
    public partial class LoaderForm : Form
    {
        public StructureLoader StructureLoader { get; set; }
        public string LastOpenedFileName { get; set; }
        public LoaderForm()
        {
            InitializeComponent();
        }

        private void openFileToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // do nothing special
        }

        private void applyButton_Click(object sender, EventArgs e)
        {
			// write current text and speaker in dictionary to the node number
			//string newText = StructureLoader.DetailsDictionary[StructureLoader.LastNodeNumber].Replace("\"" + StructureLoader.LastNodeText + "\"", "\"" + textTB.Text + "\"").Replace("\"" + StructureLoader.LastNodeSpeaker + "\"", "\"" + speakerTB.Text + "\"");
			string newText = RawViewTB.Text;
			StructureLoader.DetailsDictionary[StructureLoader.LastNodeNumber] = newText;

            // update the treeview
            if (StructureLoader.LastNode != null)
            { 
                // TODO: sometimes this is null, not sure what the implication is...
                StructureLoader.LastNode.Text = newText.Substring(0, 50);
            }

            StructureLoader.CreateTreeViewFromDictionary(StructureLoader.DetailsDictionary);


            applyButton.Enabled = false;

        }

        private void openFileToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            //TODO: temporary
            Config.InitialPath = @"C:\Users\mtr\Source\Repos\GardanZero\HS_VNFrame_ScriptHelper\HS_VNFrame_ScriptHelper\Scripts\";
            openFileDialog1.Filter = "Python Files | *.py";
            openFileDialog1.InitialDirectory = Config.InitialPath;
            DialogResult dialogResult = openFileDialog1.ShowDialog();

            // this is the selected file

            LastOpenedFileName = openFileDialog1.FileName;
            StructureLoader = new StructureLoader(LastOpenedFileName, this);
            StructureLoader.LoadStructure();
        }

        private void saveToFileToolStripMenuItem_Click(object sender, EventArgs e)
        {
            StructureLoader.LoaderForm.saveFileDialog1.Filter = "Python Files | *.py";
            StructureLoader.LoaderForm.saveFileDialog1.InitialDirectory = Config.InitialPath;
            StructureLoader.LoaderForm.saveFileDialog1.FileName = LastOpenedFileName.Substring(LastOpenedFileName.IndexOf(".")) + "_new.py";
            DialogResult dialogResult = StructureLoader.LoaderForm.saveFileDialog1.ShowDialog();

            string saveFileFullPath = StructureLoader.LoaderForm.saveFileDialog1.FileName;

            SaveFile(saveFileFullPath);
        }

        public void SaveFile(string saveFileFullPath)
        {
            // read dictionary and write to file
            StringBuilder sb = new StringBuilder();

            foreach (string dictKey in StructureLoader.DetailsDictionary.Keys)
            {
                if (dictKey == ("0.0"))
                {
                    sb.Append(StructureLoader.DetailsDictionary[dictKey]);
                }
                else if (!dictKey.Contains(".0"))
                {
                    sb.Append(StructureLoader.DetailsDictionary[dictKey]);
                }
            }

            File.WriteAllText(saveFileFullPath, sb.ToString());

            int i = 8;
        }

		private void RawViewTB_KeyUp(object sender, KeyEventArgs e)
		{
			this.applyButton.Enabled = true;
		}
	}
}
