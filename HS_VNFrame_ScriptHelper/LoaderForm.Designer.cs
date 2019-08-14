namespace HS_VNFrame_ScriptHelper
{
    partial class LoaderForm
    {

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        public void InitializeComponent()
        {
			this.components = new System.ComponentModel.Container();
			this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
			this.menuStrip1 = new System.Windows.Forms.MenuStrip();
			this.openFileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.openFileToolStripMenuItem1 = new System.Windows.Forms.ToolStripMenuItem();
			this.saveToFileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.configToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.structureTreeView = new System.Windows.Forms.TreeView();
			this.RawViewTB = new System.Windows.Forms.TextBox();
			this.label1 = new System.Windows.Forms.Label();
			this.label2 = new System.Windows.Forms.Label();
			this.speakerTB = new System.Windows.Forms.TextBox();
			this.textTB = new System.Windows.Forms.TextBox();
			this.label3 = new System.Windows.Forms.Label();
			this.label4 = new System.Windows.Forms.Label();
			this.button1 = new System.Windows.Forms.Button();
			this.sceneDirTB = new System.Windows.Forms.TextBox();
			this.label5 = new System.Windows.Forms.Label();
			this.label6 = new System.Windows.Forms.Label();
			this.pngTB = new System.Windows.Forms.TextBox();
			this.contextMenuStrip1 = new System.Windows.Forms.ContextMenuStrip(this.components);
			this.saveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
			this.jumpToSceneTB = new System.Windows.Forms.TextBox();
			this.toSceneLabel = new System.Windows.Forms.Label();
			this.menuStrip1.SuspendLayout();
			this.SuspendLayout();
			// 
			// openFileDialog1
			// 
			this.openFileDialog1.FileName = "openFileDialog1";
			// 
			// menuStrip1
			// 
			this.menuStrip1.ImageScalingSize = new System.Drawing.Size(24, 24);
			this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.openFileToolStripMenuItem,
            this.configToolStripMenuItem});
			this.menuStrip1.Location = new System.Drawing.Point(0, 0);
			this.menuStrip1.Name = "menuStrip1";
			this.menuStrip1.Padding = new System.Windows.Forms.Padding(9, 3, 0, 3);
			this.menuStrip1.Size = new System.Drawing.Size(1924, 35);
			this.menuStrip1.TabIndex = 0;
			this.menuStrip1.Text = "menuStrip1";
			// 
			// openFileToolStripMenuItem
			// 
			this.openFileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.openFileToolStripMenuItem1,
            this.saveToFileToolStripMenuItem});
			this.openFileToolStripMenuItem.Name = "openFileToolStripMenuItem";
			this.openFileToolStripMenuItem.Size = new System.Drawing.Size(50, 29);
			this.openFileToolStripMenuItem.Text = "File";
			this.openFileToolStripMenuItem.Click += new System.EventHandler(this.openFileToolStripMenuItem_Click);
			// 
			// openFileToolStripMenuItem1
			// 
			this.openFileToolStripMenuItem1.Name = "openFileToolStripMenuItem1";
			this.openFileToolStripMenuItem1.Size = new System.Drawing.Size(187, 30);
			this.openFileToolStripMenuItem1.Text = "Open File";
			this.openFileToolStripMenuItem1.Click += new System.EventHandler(this.openFileToolStripMenuItem1_Click);
			// 
			// saveToFileToolStripMenuItem
			// 
			this.saveToFileToolStripMenuItem.Name = "saveToFileToolStripMenuItem";
			this.saveToFileToolStripMenuItem.Size = new System.Drawing.Size(187, 30);
			this.saveToFileToolStripMenuItem.Text = "Save To File";
			this.saveToFileToolStripMenuItem.Click += new System.EventHandler(this.saveToFileToolStripMenuItem_Click);
			// 
			// configToolStripMenuItem
			// 
			this.configToolStripMenuItem.Name = "configToolStripMenuItem";
			this.configToolStripMenuItem.Size = new System.Drawing.Size(77, 29);
			this.configToolStripMenuItem.Text = "Config";
			// 
			// structureTreeView
			// 
			this.structureTreeView.Location = new System.Drawing.Point(20, 85);
			this.structureTreeView.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
			this.structureTreeView.Name = "structureTreeView";
			this.structureTreeView.Size = new System.Drawing.Size(536, 1246);
			this.structureTreeView.TabIndex = 1;
			// 
			// RawViewTB
			// 
			this.RawViewTB.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.RawViewTB.Location = new System.Drawing.Point(602, 85);
			this.RawViewTB.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
			this.RawViewTB.Multiline = true;
			this.RawViewTB.Name = "RawViewTB";
			this.RawViewTB.ScrollBars = System.Windows.Forms.ScrollBars.Both;
			this.RawViewTB.Size = new System.Drawing.Size(1432, 406);
			this.RawViewTB.TabIndex = 2;
			// 
			// label1
			// 
			this.label1.AutoSize = true;
			this.label1.Location = new System.Drawing.Point(20, 55);
			this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
			this.label1.Name = "label1";
			this.label1.Size = new System.Drawing.Size(75, 20);
			this.label1.TabIndex = 3;
			this.label1.Text = "Structure";
			// 
			// label2
			// 
			this.label2.AutoSize = true;
			this.label2.Location = new System.Drawing.Point(597, 60);
			this.label2.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
			this.label2.Name = "label2";
			this.label2.Size = new System.Drawing.Size(141, 20);
			this.label2.TabIndex = 4;
			this.label2.Text = "Details - Raw View";
			// 
			// speakerTB
			// 
			this.speakerTB.Location = new System.Drawing.Point(698, 554);
			this.speakerTB.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
			this.speakerTB.Name = "speakerTB";
			this.speakerTB.Size = new System.Drawing.Size(148, 26);
			this.speakerTB.TabIndex = 5;
			// 
			// textTB
			// 
			this.textTB.Location = new System.Drawing.Point(698, 589);
			this.textTB.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
			this.textTB.Multiline = true;
			this.textTB.Name = "textTB";
			this.textTB.ScrollBars = System.Windows.Forms.ScrollBars.Both;
			this.textTB.Size = new System.Drawing.Size(1336, 142);
			this.textTB.TabIndex = 6;
			// 
			// label3
			// 
			this.label3.AutoSize = true;
			this.label3.Location = new System.Drawing.Point(602, 558);
			this.label3.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
			this.label3.Name = "label3";
			this.label3.Size = new System.Drawing.Size(69, 20);
			this.label3.TabIndex = 7;
			this.label3.Text = "Speaker";
			// 
			// label4
			// 
			this.label4.AutoSize = true;
			this.label4.Location = new System.Drawing.Point(602, 594);
			this.label4.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
			this.label4.Name = "label4";
			this.label4.Size = new System.Drawing.Size(39, 20);
			this.label4.TabIndex = 8;
			this.label4.Text = "Text";
			// 
			// button1
			// 
			this.button1.Location = new System.Drawing.Point(602, 502);
			this.button1.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
			this.button1.Name = "button1";
			this.button1.Size = new System.Drawing.Size(158, 43);
			this.button1.TabIndex = 9;
			this.button1.Text = "Apply Changes";
			this.button1.UseVisualStyleBackColor = true;
			this.button1.Click += new System.EventHandler(this.saveButton_Click);
			// 
			// sceneDirTB
			// 
			this.sceneDirTB.Location = new System.Drawing.Point(698, 745);
			this.sceneDirTB.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
			this.sceneDirTB.Name = "sceneDirTB";
			this.sceneDirTB.Size = new System.Drawing.Size(148, 26);
			this.sceneDirTB.TabIndex = 10;
			// 
			// label5
			// 
			this.label5.AutoSize = true;
			this.label5.Location = new System.Drawing.Point(602, 749);
			this.label5.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
			this.label5.Name = "label5";
			this.label5.Size = new System.Drawing.Size(72, 20);
			this.label5.TabIndex = 11;
			this.label5.Text = "sceneDir";
			// 
			// label6
			// 
			this.label6.AutoSize = true;
			this.label6.Location = new System.Drawing.Point(602, 789);
			this.label6.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
			this.label6.Name = "label6";
			this.label6.Size = new System.Drawing.Size(43, 20);
			this.label6.TabIndex = 12;
			this.label6.Text = "PNG";
			// 
			// pngTB
			// 
			this.pngTB.Location = new System.Drawing.Point(698, 785);
			this.pngTB.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
			this.pngTB.Name = "pngTB";
			this.pngTB.Size = new System.Drawing.Size(148, 26);
			this.pngTB.TabIndex = 13;
			// 
			// contextMenuStrip1
			// 
			this.contextMenuStrip1.ImageScalingSize = new System.Drawing.Size(24, 24);
			this.contextMenuStrip1.Name = "contextMenuStrip1";
			this.contextMenuStrip1.Size = new System.Drawing.Size(61, 4);
			// 
			// jumpToSceneTB
			// 
			this.jumpToSceneTB.Location = new System.Drawing.Point(698, 820);
			this.jumpToSceneTB.Name = "jumpToSceneTB";
			this.jumpToSceneTB.Size = new System.Drawing.Size(148, 26);
			this.jumpToSceneTB.TabIndex = 14;
			// 
			// toSceneLabel
			// 
			this.toSceneLabel.AutoSize = true;
			this.toSceneLabel.Location = new System.Drawing.Point(602, 826);
			this.toSceneLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
			this.toSceneLabel.Name = "toSceneLabel";
			this.toSceneLabel.Size = new System.Drawing.Size(69, 20);
			this.toSceneLabel.TabIndex = 15;
			this.toSceneLabel.Text = "toScene";
			// 
			// LoaderForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(1924, 1050);
			this.Controls.Add(this.toSceneLabel);
			this.Controls.Add(this.jumpToSceneTB);
			this.Controls.Add(this.pngTB);
			this.Controls.Add(this.label6);
			this.Controls.Add(this.label5);
			this.Controls.Add(this.sceneDirTB);
			this.Controls.Add(this.button1);
			this.Controls.Add(this.label4);
			this.Controls.Add(this.label3);
			this.Controls.Add(this.textTB);
			this.Controls.Add(this.speakerTB);
			this.Controls.Add(this.label2);
			this.Controls.Add(this.label1);
			this.Controls.Add(this.RawViewTB);
			this.Controls.Add(this.structureTreeView);
			this.Controls.Add(this.menuStrip1);
			this.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
			this.Name = "LoaderForm";
			this.Text = "VNFrame ScriptHelper";
			this.menuStrip1.ResumeLayout(false);
			this.menuStrip1.PerformLayout();
			this.ResumeLayout(false);
			this.PerformLayout();

        }

        #endregion

        public System.Windows.Forms.OpenFileDialog openFileDialog1;
        public System.Windows.Forms.MenuStrip menuStrip1;
        public System.Windows.Forms.ToolStripMenuItem openFileToolStripMenuItem;
        public System.Windows.Forms.ToolStripMenuItem configToolStripMenuItem;
        public System.Windows.Forms.TreeView structureTreeView;
        public System.Windows.Forms.TextBox RawViewTB;
        public System.Windows.Forms.Label label1;
        public System.Windows.Forms.Label label2;
        public System.Windows.Forms.TextBox speakerTB;
        public System.Windows.Forms.TextBox textTB;
        public System.Windows.Forms.Label label3;
        public System.Windows.Forms.Label label4;
        public System.Windows.Forms.Button button1;
        public System.Windows.Forms.ToolStripMenuItem openFileToolStripMenuItem1;
        public System.Windows.Forms.ToolStripMenuItem saveToFileToolStripMenuItem;
        public System.Windows.Forms.TextBox sceneDirTB;
        public System.Windows.Forms.Label label5;
        public System.Windows.Forms.Label label6;
        public System.Windows.Forms.TextBox pngTB;
        public System.Windows.Forms.ContextMenuStrip contextMenuStrip1;
        private System.ComponentModel.IContainer components;
        private System.Windows.Forms.SaveFileDialog saveFileDialog1;
		public System.Windows.Forms.TextBox jumpToSceneTB;
		public System.Windows.Forms.Label toSceneLabel;
	}
}

