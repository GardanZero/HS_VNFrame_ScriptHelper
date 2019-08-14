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
				jumpToLocation = currentString.Substring(lastIndexOfSpace, lastIndexOfBracket - lastIndexOfSpace);
			}
			catch
			{

			}

			return jumpToLocation;
		}

	}
}
