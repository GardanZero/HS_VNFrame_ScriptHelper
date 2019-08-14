using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using HS_VNFrame_ScriptHelper;
using System.IO;

namespace ScriptHelper_TestProject
{
    [TestClass]
    public class UnitTestScriptHelper
    {
        [TestMethod]
        public void TestFileInputEqualsOutput()
        {
            string testFile = @"C:\Users\mtr\Source\Repos\GardanZero\HS_VNFrame_ScriptHelper\HS_VNFrame_ScriptHelper\Scripts\fun2";
			LoaderForm loaderForm = new LoaderForm();

            loaderForm.StructureLoader = new StructureLoader(testFile+".py", loaderForm);
            loaderForm.StructureLoader.LoadStructure();

            loaderForm.SaveFile(testFile+"_unitTest.py");

            string origFileText = File.ReadAllText(testFile + ".py");
            string testFileText = File.ReadAllText(testFile+"_unitTest.py");

            if (origFileText == testFileText)
            {
                Assert.AreEqual(origFileText, testFileText);
            }
            else
            {
                Assert.Fail("The input and output file text does not match.");
            }

            // cleanup
            File.Delete(testFile + "_unitTest.py");
        }
    }
}
