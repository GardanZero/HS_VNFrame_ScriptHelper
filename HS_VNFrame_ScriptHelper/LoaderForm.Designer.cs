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
			this.applyButton = new System.Windows.Forms.Button();
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
			this.menuStrip1.Padding = new System.Windows.Forms.Padding(8, 2, 0, 2);
			this.menuStrip1.Size = new System.Drawing.Size(1710, 28);
			this.menuStrip1.TabIndex = 0;
			this.menuStrip1.Text = "menuStrip1";
			// 
			// openFileToolStripMenuItem
			// 
			this.openFileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.openFileToolStripMenuItem1,
            this.saveToFileToolStripMenuItem});
			this.openFileToolStripMenuItem.Name = "openFileToolStripMenuItem";
			this.openFileToolStripMenuItem.Size = new System.Drawing.Size(44, 24);
			this.openFileToolStripMenuItem.Text = "File";
			this.openFileToolStripMenuItem.Click += new System.EventHandler(this.openFileToolStripMenuItem_Click);
			// 
			// openFileToolStripMenuItem1
			// 
			this.openFileToolStripMenuItem1.Name = "openFileToolStripMenuItem1";
			this.openFileToolStripMenuItem1.Size = new System.Drawing.Size(162, 26);
			this.openFileToolStripMenuItem1.Text = "Open File";
			this.openFileToolStripMenuItem1.Click += new System.EventHandler(this.openFileToolStripMenuItem1_Click);
			// 
			// saveToFileToolStripMenuItem
			// 
			this.saveToFileToolStripMenuItem.Name = "saveToFileToolStripMenuItem";
			this.saveToFileToolStripMenuItem.Size = new System.Drawing.Size(162, 26);
			this.saveToFileToolStripMenuItem.Text = "Save To File";
			this.saveToFileToolStripMenuItem.Click += new System.EventHandler(this.saveToFileToolStripMenuItem_Click);
			// 
			// configToolStripMenuItem
			// 
			this.configToolStripMenuItem.Name = "configToolStripMenuItem";
			this.configToolStripMenuItem.Size = new System.Drawing.Size(65, 24);
			this.configToolStripMenuItem.Text = "Config";
			// 
			// structureTreeView
			// 
			this.structureTreeView.Location = new System.Drawing.Point(18, 68);
			this.structureTreeView.Margin = new System.Windows.Forms.Padding(4);
			this.structureTreeView.Name = "structureTreeView";
			this.structureTreeView.Size = new System.Drawing.Size(477, 998);
			this.structureTreeView.TabIndex = 1;
			// 
			// RawViewTB
			// 
			this.RawViewTB.Font = new System.Drawing.Font("Courier New", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.RawViewTB.Location = new System.Drawing.Point(535, 68);
			this.RawViewTB.Margin = new System.Windows.Forms.Padding(4);
			this.RawViewTB.Multiline = true;
			this.RawViewTB.Name = "RawViewTB";
			this.RawViewTB.ScrollBars = System.Windows.Forms.ScrollBars.Both;
			this.RawViewTB.Size = new System.Drawing.Size(1273, 326);
			this.RawViewTB.TabIndex = 2;
			this.RawViewTB.KeyUp += new System.Windows.Forms.KeyEventHandler(this.RawViewTB_KeyUp);
			// 
			// label1
			// 
			this.label1.AutoSize = true;
			this.label1.Location = new System.Drawing.Point(18, 44);
			this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
			this.label1.Name = "label1";
			this.label1.Size = new System.Drawing.Size(66, 17);
			this.label1.TabIndex = 3;
			this.label1.Text = "Structure";
			// 
			// label2
			// 
			this.label2.AutoSize = true;
			this.label2.Location = new System.Drawing.Point(531, 48);
			this.label2.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
			this.label2.Name = "label2";
			this.label2.Size = new System.Drawing.Size(124, 17);
			this.label2.TabIndex = 4;
			this.label2.Text = "Details - Raw View";
			// 
			// speakerTB
			// 
			this.speakerTB.Location = new System.Drawing.Point(620, 443);
			this.speakerTB.Margin = new System.Windows.Forms.Padding(4);
			this.speakerTB.Name = "speakerTB";
			this.speakerTB.Size = new System.Drawing.Size(132, 22);
			this.speakerTB.TabIndex = 5;
			this.speakerTB.Visible = false;
			// 
			// textTB
			// 
			this.textTB.Location = new System.Drawing.Point(620, 471);
			this.textTB.Margin = new System.Windows.Forms.Padding(4);
			this.textTB.Multiline = true;
			this.textTB.Name = "textTB";
			this.textTB.ScrollBars = System.Windows.Forms.ScrollBars.Both;
			this.textTB.Size = new System.Drawing.Size(1188, 114);
			this.textTB.TabIndex = 6;
			this.textTB.Visible = false;
			// 
			// label3
			// 
			this.label3.AutoSize = true;
			this.label3.Location = new System.Drawing.Point(535, 446);
			this.label3.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
			this.label3.Name = "label3";
			this.label3.Size = new System.Drawing.Size(61, 17);
			this.label3.TabIndex = 7;
			this.label3.Text = "Speaker";
			// 
			// label4
			// 
			this.label4.AutoSize = true;
			this.label4.Location = new System.Drawing.Point(535, 475);
			this.label4.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
			this.label4.Name = "label4";
			this.label4.Size = new System.Drawing.Size(35, 17);
			this.label4.TabIndex = 8;
			this.label4.Text = "Text";
			// 
			// applyButton
			// 
			this.applyButton.Enabled = false;
			this.applyButton.Location = new System.Drawing.Point(535, 402);
			this.applyButton.Margin = new System.Windows.Forms.Padding(4);
			this.applyButton.Name = "applyButton";
			this.applyButton.Size = new System.Drawing.Size(140, 34);
			this.applyButton.TabIndex = 9;
			this.applyButton.Text = "Apply Changes";
			this.applyButton.UseVisualStyleBackColor = true;
			this.applyButton.Click += new System.EventHandler(this.applyButton_Click);
			// 
			// sceneDirTB
			// 
			this.sceneDirTB.Location = new System.Drawing.Point(620, 596);
			this.sceneDirTB.Margin = new System.Windows.Forms.Padding(4);
			this.sceneDirTB.Name = "sceneDirTB";
			this.sceneDirTB.Size = new System.Drawing.Size(132, 22);
			this.sceneDirTB.TabIndex = 10;
			// 
			// label5
			// 
			this.label5.AutoSize = true;
			this.label5.Location = new System.Drawing.Point(535, 599);
			this.label5.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
			this.label5.Name = "label5";
			this.label5.Size = new System.Drawing.Size(64, 17);
			this.label5.TabIndex = 11;
			this.label5.Text = "sceneDir";
			// 
			// label6
			// 
			this.label6.AutoSize = true;
			this.label6.Location = new System.Drawing.Point(535, 631);
			this.label6.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
			this.label6.Name = "label6";
			this.label6.Size = new System.Drawing.Size(38, 17);
			this.label6.TabIndex = 12;
			this.label6.Text = "PNG";
			// 
			// pngTB
			// 
			this.pngTB.Location = new System.Drawing.Point(620, 628);
			this.pngTB.Margin = new System.Windows.Forms.Padding(4);
			this.pngTB.Name = "pngTB";
			this.pngTB.Size = new System.Drawing.Size(132, 22);
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
			this.jumpToSceneTB.Location = new System.Drawing.Point(620, 656);
			this.jumpToSceneTB.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
			this.jumpToSceneTB.Name = "jumpToSceneTB";
			this.jumpToSceneTB.Size = new System.Drawing.Size(132, 22);
			this.jumpToSceneTB.TabIndex = 14;
			// 
			// toSceneLabel
			// 
			this.toSceneLabel.AutoSize = true;
			this.toSceneLabel.Location = new System.Drawing.Point(535, 661);
			this.toSceneLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
			this.toSceneLabel.Name = "toSceneLabel";
			this.toSceneLabel.Size = new System.Drawing.Size(60, 17);
			this.toSceneLabel.TabIndex = 15;
			this.toSceneLabel.Text = "toScene";
			// 
			// LoaderForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(1710, 840);
			this.Controls.Add(this.toSceneLabel);
			this.Controls.Add(this.jumpToSceneTB);
			this.Controls.Add(this.pngTB);
			this.Controls.Add(this.label6);
			this.Controls.Add(this.label5);
			this.Controls.Add(this.sceneDirTB);
			this.Controls.Add(this.applyButton);
			this.Controls.Add(this.label4);
			this.Controls.Add(this.label3);
			this.Controls.Add(this.textTB);
			this.Controls.Add(this.speakerTB);
			this.Controls.Add(this.label2);
			this.Controls.Add(this.label1);
			this.Controls.Add(this.RawViewTB);
			this.Controls.Add(this.structureTreeView);
			this.Controls.Add(this.menuStrip1);
			this.Margin = new System.Windows.Forms.Padding(4);
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
        public System.Windows.Forms.Button applyButton;
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

