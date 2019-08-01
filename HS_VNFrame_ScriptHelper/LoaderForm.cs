using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace HS_VNFrame_ScriptHelper
{
    public partial class LoaderForm : Form
    {
        public StructureLoader StructureLoader { get; set; }

        public LoaderForm()
        {
            InitializeComponent();
        }

        private void openFileToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // do nothing special
        }

        private void saveButton_Click(object sender, EventArgs e)
        {
            // write current text and speaker in dictionary to the node number
            string newText = StructureLoader.DetailsDictionary[StructureLoader.LastNodeNumber].Replace("\"" + StructureLoader.LastNodeText + "\"", "\"" + textTB.Text + "\"").Replace("\"" + StructureLoader.LastNodeSpeaker + "\"", "\"" + speakerTB.Text + "\"");
            StructureLoader.DetailsDictionary[StructureLoader.LastNodeNumber] = newText;

            // update the treeview
            StructureLoader.LastNode.Text = newText.Substring(0, 50);

        }

        private void openFileToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            //TODO: temporary
            Config.InitialPath = @"E:\Games\H\Honey Select FR2 - FlashBangZ\Plugins\Console\Lib\";
            openFileDialog1.Filter = "Python Files | *.py";
            openFileDialog1.InitialDirectory = Config.InitialPath;
            DialogResult dialogResult = openFileDialog1.ShowDialog();

            // this is the selected file
            string filename = openFileDialog1.FileName;
            StructureLoader = new StructureLoader(filename, this);
            StructureLoader.LoadStructure();
        }
    }
}
