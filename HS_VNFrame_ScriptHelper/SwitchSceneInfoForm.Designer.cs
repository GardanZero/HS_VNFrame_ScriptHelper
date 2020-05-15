namespace HS_VNFrame_ScriptHelper
{
    partial class SwitchSceneInfoForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

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
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.filenameTB = new System.Windows.Forms.TextBox();
            this.SeqNameTB = new System.Windows.Forms.TextBox();
            this.OKbtn = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.switchSceneNameTB = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(25, 80);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(433, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "What is the name of the .png file you want to load? (no path, just filenamem incl" +
    "uding .png)";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(28, 147);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(405, 13);
            this.label2.TabIndex = 1;
            this.label2.Text = "What is the name of the Seq you want to jump to in the new scene? (default toSeq1" +
    ")";
            // 
            // filenameTB
            // 
            this.filenameTB.Location = new System.Drawing.Point(491, 77);
            this.filenameTB.Name = "filenameTB";
            this.filenameTB.Size = new System.Drawing.Size(204, 20);
            this.filenameTB.TabIndex = 2;
            // 
            // SeqNameTB
            // 
            this.SeqNameTB.Location = new System.Drawing.Point(491, 144);
            this.SeqNameTB.Name = "SeqNameTB";
            this.SeqNameTB.Size = new System.Drawing.Size(204, 20);
            this.SeqNameTB.TabIndex = 3;
            this.SeqNameTB.Text = "toSeq1";
            // 
            // OKbtn
            // 
            this.OKbtn.Location = new System.Drawing.Point(620, 196);
            this.OKbtn.Name = "OKbtn";
            this.OKbtn.Size = new System.Drawing.Size(75, 23);
            this.OKbtn.TabIndex = 4;
            this.OKbtn.Text = "OK";
            this.OKbtn.UseVisualStyleBackColor = true;
            this.OKbtn.Click += new System.EventHandler(this.OKbtn_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(31, 13);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(303, 13);
            this.label3.TabIndex = 5;
            this.label3.Text = "What do you want to call the switch scene node in the .py file?";
            // 
            // switchSceneNameTB
            // 
            this.switchSceneNameTB.Location = new System.Drawing.Point(491, 10);
            this.switchSceneNameTB.Name = "switchSceneNameTB";
            this.switchSceneNameTB.Size = new System.Drawing.Size(204, 20);
            this.switchSceneNameTB.TabIndex = 6;
            this.switchSceneNameTB.Text = "switchToScene_2";
            // 
            // SwitchSceneInfoForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(707, 243);
            this.Controls.Add(this.switchSceneNameTB);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.OKbtn);
            this.Controls.Add(this.SeqNameTB);
            this.Controls.Add(this.filenameTB);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "SwitchSceneInfoForm";
            this.Text = "SwitchSceneInfoForm";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        public System.Windows.Forms.TextBox filenameTB;
        public System.Windows.Forms.TextBox SeqNameTB;
        private System.Windows.Forms.Button OKbtn;
        private System.Windows.Forms.Label label3;
        public System.Windows.Forms.TextBox switchSceneNameTB;
    }
}