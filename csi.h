/**
*	Define some of the CSI Codes for terminal control.
#	See: http://en.wikipedia.org/wiki/ANSI_escape_code
*	When use, statically concatenate the macro and string.
*	eg. printf(CSI_UTIL_CLR_RED"Red.\n"CSI_UTIL_RESET);
		printf("\e[A\e[K") <=> printf(CSI_CUU(1) CSI_EL(0)); 
			(moving cursor up a line and clear that line.)
*	Author: John Zhang
*/

#define CSI	"\e[" //Control Sequence Introducer, start of CSI sequence

/**
*	Cursor controls.
*/
#define CSI_CUU(N) CSI #N "A" //Cursor Up (default 1)
#define CSI_CUD(N) CSI #N "B" //Cursor Down (default 1)
#define CSI_CUF(N) CSI #N "C" //Cursor Forward (default 1)
#define CSI_CUB(N) CSI #N "D" //Cursor Back (default 1)
#define CSI_CNL(N) CSI #N "E" //Cursor Next Line: Move cursor to beginning of N (default 1) lines down.
#define CSI_CPL(N) CSI #N "F" //Cursor Previous Line: Move cursor to beginning of N (default 1) lines up.
#define CSI_CHA(N) CSI #N "G" //Cursor Horizontal Absolute: Move to column n
#define CSI_CUP(N,M) CSI #N ; #M "H" //Moves the cursor to row n, column m. The values are 1-based, and default to 1 (top left corner) if omitted. A sequence such as CSI ;5H is a synonym for CSI 1;5H as well as CSI 17;H is the same as CSI 17H and CSI 17;1H
#define CSI_ED(N) CSI #N "J" //Clears part of the screen. If n is zero (or missing), clear from cursor to end of screen. If n is one, clear from cursor to beginning of the screen. If n is two, clear entire screen (and moves cursor to upper left on MS-DOS ANSI.SYS).
#define CSI_EL(N) CSI #N "K" //Erases part of the line. If n is zero (or missing), clear from cursor to the end of the line. If n is one, clear from cursor to beginning of the line. If n is two, clear entire line. Cursor position does not change.
#define CSI_SU(N) CSI #N "S" //Scroll whole page up by n (default 1) lines. New lines are added at the bottom. (not ANSI.SYS)
#define CSI_SD(N) CSI #N "T" //Scroll whole page down by n (default 1) lines. New lines are added at the top. (not ANSI.SYS)
#define CSI_HVP(N,M) CSI_CUP(N,M)

/**
*	SGR (Select Graphic Rendition) Parameters
*	NOTE: SKIPPED SOME NOT WIDELY SUPPORTED CODES.
*/
#define STR(S)	#S
#define CSI_SGR(N) CSI STR(N) "m"
//POSSIBLE VALUES FOR N
#define CSI_SGR_PARAM_RESET									0	//All attributes off
#define CSI_SGR_PARAM_BOLD									1	
#define CSI_SGR_PARAM_FAINT									2	//Not widely supported
#define CSI_SGR_PARAM_ITALIC_ON								3	//Not widely supported, sometimes treated as inverse
#define CSI_SGR_PARAM_UNDERLINE_SINGLE						4
#define CSI_SGR_PARAM_BLINK_SLOW							5
#define CSI_SGR_PARAM_BLINK_RAPID							6
#define CSI_SGR_PARAM_IMAGE_NEGATIVE						7	//Inverse or reverse; swap foreground and background.
#define CSI_SGR_PARAM_FONT_PRIME							10
#define CSI_SGR_PARAM_FONT_ALT_1							11
#define CSI_SGR_PARAM_FONT_ALT_2							12
#define CSI_SGR_PARAM_FONT_ALT_3							13
#define CSI_SGR_PARAM_FONT_ALT_4							14
#define CSI_SGR_PARAM_FONT_ALT_5							15
#define CSI_SGR_PARAM_FONT_ALT_6							16
#define CSI_SGR_PARAM_FONT_ALT_7							17
#define CSI_SGR_PARAM_FONT_ALT_8							18
#define CSI_SGR_PARAM_FONT_ALT_9							19
#define CSI_SGR_PARAM_FONT_NORM_COLOR						22	//Neither bold nor faint
#define CSI_SGR_PARAM_NO_ITALIC_NO_FRAKUR					23
#define CSI_SGR_PARAM_UNDERLINE_NONE						24	//Not singly or doubly underlined.
#define CSI_SGR_PARAM_BLINK_OFF								25
#define CSI_SGR_PARAM_IMAGE_POSITIVE						27
#define CSI_SGR_PARAM_TEXT_CLR_BLACK						30
#define CSI_SGR_PARAM_TEXT_CLR_RED							31
#define CSI_SGR_PARAM_TEXT_CLR_GREEN						32
#define CSI_SGR_PARAM_TEXT_CLR_YELLOW						33
#define CSI_SGR_PARAM_TEXT_CLR_BLUE							34
#define CSI_SGR_PARAM_TEXT_CLR_MAGENTA						35
#define CSI_SGR_PARAM_TEXT_CLR_CYAN							36
#define CSI_SGR_PARAM_TEXT_CLR_WHITE						37
#define CSI_SGR_PARAM_TEXT_CLR_DEFAULT						39
#define CSI_SGR_PARAM_BG_CLR_BLACK							40
#define CSI_SGR_PARAM_BG_CLR_RED							41
#define CSI_SGR_PARAM_BG_CLR_GREEN							42
#define CSI_SGR_PARAM_BG_CLR_YELLOW							43
#define CSI_SGR_PARAM_BG_CLR_BLUE							44
#define CSI_SGR_PARAM_BG_CLR_MAGENTA						45
#define CSI_SGR_PARAM_BG_CLR_CYAN							46
#define CSI_SGR_PARAM_BG_CLR_WHITE							47
#define CSI_SGR_PARAM_BG_CLR_DEFAULT						49

#define CSI_DSR CSI "6" "n" //Reports the cursor position to the application as (as though typed at the keyboard) ESC[n;mR, where n is the row and m is the column. (May not work on MS-DOS.)
#define CSI_SCP CSI "s" //Save cursor position
#define CSI_RCP CSI "u" //Restores the cursor position
#define CSI_CUHIDE	CSI "?25!"	//Hides the cursor (trailing character is lowercase L.)
#define CSI_CUSHOW	CSI "?25h"	//Shows the cursor

/**
*	Utilising Colour Printing
*/
#define CSI_UTIL_CLR_DEFAULT	CSI_SGR(CSI_SGR_PARAM_TEXT_CLR_DEFAULT)
#define CSI_UTIL_CLR_BLACK		CSI_SGR(CSI_SGR_PARAM_TEXT_CLR_BLACK)
#define CSI_UTIL_CLR_RED		CSI_SGR(CSI_SGR_PARAM_TEXT_CLR_RED)
#define CSI_UTIL_CLR_GREEN		CSI_SGR(CSI_SGR_PARAM_TEXT_CLR_GREEN)
#define CSI_UTIL_CLR_YELLOW		CSI_SGR(CSI_SGR_PARAM_TEXT_CLR_YELLOW)
#define CSI_UTIL_CLR_BLUE		CSI_SGR(CSI_SGR_PARAM_TEXT_CLR_BLUE)
#define CSI_UTIL_CLR_MAGENTA	CSI_SGR(CSI_SGR_PARAM_TEXT_CLR_MAGENTA)
#define CSI_UTIL_CLR_CYAN		CSI_SGR(CSI_SGR_PARAM_TEXT_CLR_CYAN)
#define CSI_UTIL_CLR_WHITE		CSI_SGR(CSI_SGR_PARAM_TEXT_CLR_WHITE)

#define CSI_UTIL_CLR_BLACK_BOLD		CSI_SGR(CSI_SGR_PARAM_TEXT_CLR_BLACK;CSI_SGR_PARAM_BOLD)
#define CSI_UTIL_CLR_RED_BOLD		CSI_SGR(CSI_SGR_PARAM_TEXT_CLR_RED;CSI_SGR_PARAM_BOLD)
#define CSI_UTIL_CLR_GREEN_BOLD		CSI_SGR(CSI_SGR_PARAM_TEXT_CLR_GREEN;CSI_SGR_PARAM_BOLD)
#define CSI_UTIL_CLR_YELLOW_BOLD	CSI_SGR(CSI_SGR_PARAM_TEXT_CLR_YELLOW;CSI_SGR_PARAM_BOLD)
#define CSI_UTIL_CLR_BLUE_BOLD		CSI_SGR(CSI_SGR_PARAM_TEXT_CLR_BLUE;CSI_SGR_PARAM_BOLD)
#define CSI_UTIL_CLR_MAGENTA_BOLD	CSI_SGR(CSI_SGR_PARAM_TEXT_CLR_MAGENTA;CSI_SGR_PARAM_BOLD)
#define CSI_UTIL_CLR_CYAN_BOLD		CSI_SGR(CSI_SGR_PARAM_TEXT_CLR_CYAN;CSI_SGR_PARAM_BOLD)
#define CSI_UTIL_CLR_WHITE_BOLD		CSI_SGR(CSI_SGR_PARAM_TEXT_CLR_WHITE;CSI_SGR_PARAM_BOLD)
#define CSI_UTIL_BOLD		CSI_SGR(CSI_SGR_PARAM_BOLD)
#define CSI_UTIL_RESET				CSI_SGR(CSI_SGR_PARAM_RESET)

#define CSI_STR_BLACK(str)  CSI_UTIL_CLR_BLACK str CSI_UTIL_RESET
#define CSI_STR_RED(str)    CSI_UTIL_CLR_RED str CSI_UTIL_RESET
#define CSI_STR_GREEN(str)  CSI_UTIL_CLR_GREEN str CSI_UTIL_RESET
#define CSI_STR_YELLOW(str) CSI_UTIL_CLR_YELLOW str CSI_UTIL_RESET
#define CSI_STR_BLUE(str)   CSI_UTIL_CLR_BLUE str CSI_UTIL_RESET
#define CSI_STR_MAGNET(str) CSI_UTIL_CLR_MAGENT str CSI_UTIL_RESET
#define CSI_STR_CYAN(str)   CSI_UTIL_CLR_CYAN str CSI_UTIL_RESET
#define CSI_STR_WHITE(str)  CSI_UTIL_CLR_WHITE str CSI_UTIL_RESET

#define CSI_STR_BLACK_BOLD(str)  CSI_UTIL_CLR_BLACK_BOLD str CSI_UTIL_RESET
#define CSI_STR_RED_BOLD(str)    CSI_UTIL_CLR_RED_BOLD str CSI_UTIL_RESET
#define CSI_STR_GREEN_BOLD(str)  CSI_UTIL_CLR_GREEN_BOLD str CSI_UTIL_RESET
#define CSI_STR_YELLOW_BOLD(str) CSI_UTIL_CLR_YELLOW_BOLD str CSI_UTIL_RESET
#define CSI_STR_BLUE_BOLD(str)   CSI_UTIL_CLR_BLUE_BOLD str CSI_UTIL_RESET
#define CSI_STR_MAGNET_BOLD(str) CSI_UTIL_CLR_MAGENT_BOLD str CSI_UTIL_RESET
#define CSI_STR_CYAN_BOLD(str)   CSI_UTIL_CLR_CYAN_BOLD str CSI_UTIL_RESET
#define CSI_STR_WHITE_BOLD(str)  CSI_UTIL_CLR_WHITE_BOLD str CSI_UTIL_RESET

