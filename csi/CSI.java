package csi;

/**
* A library for terminal control characters.
* Author: John Zhang
*/

public class CSI
{
	//Control Sequence Introducer. CSI starts with this string.
	public static final String CSI = "\033[";
	
	//Parameters for CSI SGR

	public static final String SGR_PARAM_RESET 								= "0";
	public static final String SGR_PARAM_BOLD								= "1";
	public static final String SGR_PARAM_FAINT								= "2";	
	public static final String SGR_PARAM_ITALIC_ON							= "3";	
	public static final String SGR_PARAM_UNDERLINE_SINGLE					= "4";
	public static final String SGR_PARAM_BLINK_SLOW							= "5";	
	public static final String SGR_PARAM_BLINK_RAPID						= "6";	
	public static final String SGR_PARAM_IMAGE_NEGATIVE						= "7";
	public static final String SGR_PARAM_FONT_PRIME							= "10";
	public static final String SGR_PARAM_FONT_ALT_1							= "11";
	public static final String SGR_PARAM_FONT_ALT_2							= "12";
	public static final String SGR_PARAM_FONT_ALT_3							= "13";
	public static final String SGR_PARAM_FONT_ALT_4							= "14";
	public static final String SGR_PARAM_FONT_ALT_5							= "15";
	public static final String SGR_PARAM_FONT_ALT_6							= "16";
	public static final String SGR_PARAM_FONT_ALT_7							= "17";
	public static final String SGR_PARAM_FONT_ALT_8							= "18";
	public static final String SGR_PARAM_FONT_ALT_9							= "19";
	public static final String SGR_PARAM_FONT_NORM_COLOR					= "22";	
	public static final String SGR_PARAM_NO_ITALIC_NO_FRAKUR				= "23";
	public static final String SGR_PARAM_UNDERLINE_NONE						= "24";
	public static final String SGR_PARAM_BLINK_OFF							= "25";
	public static final String SGR_PARAM_IMAGE_POSITIVE						= "27";
	public static final String SGR_PARAM_TEXT_CLR_BLACK						= "30";
	public static final String SGR_PARAM_TEXT_CLR_RED						= "31";
	public static final String SGR_PARAM_TEXT_CLR_GREEN						= "32";
	public static final String SGR_PARAM_TEXT_CLR_YELLOW					= "33";
	public static final String SGR_PARAM_TEXT_CLR_BLUE						= "34";
	public static final String SGR_PARAM_TEXT_CLR_MAGENTA					= "35";
	public static final String SGR_PARAM_TEXT_CLR_CYAN						= "36";
	public static final String SGR_PARAM_TEXT_CLR_WHITE						= "37";
	public static final String SGR_PARAM_TEXT_CLR_DEFAULT					= "39";
	public static final String SGR_PARAM_BG_CLR_BLACK						= "40";
	public static final String SGR_PARAM_BG_CLR_RED							= "41";
	public static final String SGR_PARAM_BG_CLR_GREEN						= "42";
	public static final String SGR_PARAM_BG_CLR_YELLOW						= "43";
	public static final String SGR_PARAM_BG_CLR_BLUE						= "44";
	public static final String SGR_PARAM_BG_CLR_MAGENTA						= "45";
	public static final String SGR_PARAM_BG_CLR_CYAN						= "46";
	public static final String SGR_PARAM_BG_CLR_WHITE						= "47";
	public static final String SGR_PARAM_BG_CLR_DEFAULT						= "49";
	
	public static final String SGR(String p)
	{
		return CSI + p + "m";
	}
	
	//Cursor Up
	public static final String CUU() { return CUU("1"); }
	public static final String CUU(String strParam)
	{ return CSI + strParam + "A"; }
	
	//Cursor Down
	public static final String CUD() { return CUD("1"); }
	public static final String CUD(String strParam)
	{ return CSI + strParam + "B"; }
	
	//Cursor Forward
	public static final String CUF() { return CUF("1"); }
	public static final String CUF(String strParam)
	{ return CSI + strParam + "C"; }
	
	//Cursor Back
	public static final String CUB() { return CUB("1"); }
	public static final String CUB(String strParam)
	{ return CSI + strParam + "D"; }
	
	//Cursor Next Line
	public static final String CNL() { return CNL("1"); }
	public static final String CNL(String strParam)
	{ return CSI + strParam + "E"; }
	
	//Cursor Previous Line
	public static final String CPL() { return CPL("1"); }
	public static final String CPL(String strParam)
	{ return CSI + strParam + "F"; }
	
	//Cursor Horizontal Absolute
	public static final String CHA() { return CHA("1"); }
	public static final String CHA(String strParam)
	{ return CSI + strParam + "G"; }
	
	//Moves the cursor to row n, column m. 
	//The values are 1-based, and default to 1 (top left corner) if omitted.
	//A sequence such as CSI ;5H is a synonym for CSI 1;5H 
	//as well as CSI 17;H is the same as CSI 17H and CSI 17;1H
	public static final String CUP() { return CUP("1", "1"); }
	public static final String CUP(String strN, String strM)
	{ return CSI + strN + ";" + strM + "H"; }
	
	//Clear part of screen
	//If n is zero (or missing), clear from cursor to end of screen. 
	//If n is one, clear from cursor to beginning of the screen. 
	//If n is two, clear entire screen.
	public static final String ED() { return ED("0"); }
	public static final String ED(String strParam)
	{
		if(!strParam.equals("0") && !strParam.equals("1") && 
		   !strParam.equals("2"))
			   return null;
		return CSI + strParam + "J";
	}
	
	//Erases part of the line. 
	//If n is zero (or missing), clear from cursor to the end of the line. 
	//If n is one, clear from cursor to beginning of the line. 
	//If n is two, clear entire line. Cursor position does not change.
	public static final String EL() { return EL("0"); }
	public static final String EL(String strParam)
	{
		if(!strParam.equals("0") && !strParam.equals("1") && 
		   !strParam.equals("2"))
			   return null;
		return CSI + strParam + "K";
	}
	
	//Scroll whole page up by n (default 1) lines. 
	//New lines are added at the bottom. (not ANSI.SYS)
	public static final String SU() { return SU("1"); }
	public static final String SU(String strN)
	{ return CSI + strN + "S"; }
	
	//Scroll whole page down by n (default 1) lines. 
	//New lines are added at the top.
	public static final String SD() { return SD("1"); }
	public static final String SD(String strN)
	{ return CSI + strN + "T"; }
	
	public static final String HVP(){ return CUP();}
	public static final String HVP(String strN, String strM)
	{ return CUP(strN, strM); }
	
	//Utility Strings.
	//Colour Utility
	public static final String UTIL_RESET = SGR(SGR_PARAM_RESET);
	public static final String CLR_DEFAULT = SGR(SGR_PARAM_TEXT_CLR_DEFAULT);
	public static final String CLR_BLACK = SGR(SGR_PARAM_TEXT_CLR_BLACK);
	public static final String CLR_RED = SGR(SGR_PARAM_TEXT_CLR_RED);
	public static final String CLR_GREEN = SGR(SGR_PARAM_TEXT_CLR_GREEN);
	public static final String CLR_YELLOW = SGR(SGR_PARAM_TEXT_CLR_YELLOW);
	public static final String CLR_BLUE = SGR(SGR_PARAM_TEXT_CLR_BLUE);
	public static final String CLR_MAGENTA = SGR(SGR_PARAM_TEXT_CLR_MAGENTA);
	public static final String CLR_CYAN = SGR(SGR_PARAM_TEXT_CLR_CYAN);
	public static final String CLR_WHITE = SGR(SGR_PARAM_TEXT_CLR_WHITE);

	//Bold Color
	public static final String CLR_BLACK_BOLD = SGR(SGR_PARAM_TEXT_CLR_BLACK + ";" + SGR_PARAM_BOLD);
	public static final String CLR_RED_BOLD = SGR(SGR_PARAM_TEXT_CLR_RED + ";" + SGR_PARAM_BOLD);
	public static final String CLR_GREEN_BOLD = SGR(SGR_PARAM_TEXT_CLR_GREEN + ";" + SGR_PARAM_BOLD);
	public static final String CLR_YELLOW_BOLD = SGR(SGR_PARAM_TEXT_CLR_YELLOW + ";" + SGR_PARAM_BOLD);
	public static final String CLR_BLUE_BOLD = SGR(SGR_PARAM_TEXT_CLR_BLUE + ";" + SGR_PARAM_BOLD);
	public static final String CLR_MAGENTA_BOLD = SGR(SGR_PARAM_TEXT_CLR_MAGENTA + ";" + SGR_PARAM_BOLD);
	public static final String CLR_CYAN_BOLD = SGR(SGR_PARAM_TEXT_CLR_CYAN + ";" + SGR_PARAM_BOLD);
	public static final String CLR_WHITE_BOLD = SGR(SGR_PARAM_TEXT_CLR_WHITE + ";" + SGR_PARAM_BOLD);
	
  public static void clrprintln(String s, String clr)
  {
    System.out.println(clr + s + UTIL_RESET);
  }

  public static String clrstr(String s, String clr)
  {
    return clr + s + UTIL_RESET;
  }
}
