"""
#	Define some of the _CSI Codes for terminal control.
#	See: http://en.wikipedia.org/wiki/ANSI_escape_code
#	Author: John Zhang
"""

_CSI = '\033[';

# Cursor controls


def _CSI_CUU(N): return "%s%d%s" %  (_CSI, N, "A"); # Cursor Up (default 1)
def _CSI_CUD(N): return "%s%d%s" %  (_CSI, N, "B"); # Cursor Down (default 1)
def _CSI_CUF(N): return "%s%d%s" %  (_CSI, N, "C"); # Cursor Forward (default 1)
def _CSI_CUB(N): return "%s%d%s" %  (_CSI, N, "D"); # Cursor Back (default 1)
def _CSI_CNL(N): return "%s%d%s" %  (_CSI, N, "E"); # Cursor Next Line: Move cursor to beginning of N (default 1) lines down.
def _CSI_CPL(N): return "%s%d%s" %  (_CSI, N, "F"); # Cursor Previous Line: Move cursor to beginning of N (default 1) lines up.
def _CSI_CHA(N): return "%s%d%s" %  (_CSI, N, "G"); # Cursor Horizontal Absolute: Move to column n
def _CSI_CUP(N,M): return "%s%d%s" %  (_CSI, N, "H"); # C" //Moves the cursor to row n, column m. The values are 1-based, and default to 1 (top left corner) if omitted. A sequence such as _CSI ; #5H is a synonym for _CSI 1; #5H as well as _CSI 17; #H is the same as _CSI 17H and _CSI 17; #1H
def _CSI_ED(N): return "%s%d%s" %  (_CSI, N, "J"); # Clears part of the screen. If n is zero (or missing), clear from cursor to end of screen. If n is one, clear from cursor to beginning of the screen. If n is two, clear entire screen (and moves cursor to upper left on MS-DOS ANSI.SYS).
def _CSI_EL(N): return "%s%d%s" %  (_CSI, N, "K"); # Crases part of the line. If n is zero (or missing), clear from cursor to the end of the line. If n is one, clear from cursor to beginning of the line. If n is two, clear entire line. Cursor position does not change.
def _CSI_SU(N): return "%s%d%s" %  (_CSI, N, "S"); # Ccroll whole page up by n (default 1) lines. New lines are added at the bottom. (not ANSI.SYS)
def _CSI_SD(N): return "%s%d%s" %  (_CSI, N, "T"); # Ccroll whole page down by n (default 1) lines. New lines are added at the top. (not ANSI.SYS)
def _CSI_HVP(N,M): return _CSI_CUP(N, M);


def _CSI_SGR(N): return "%s%sm" % (_CSI, N);

_CSI_SGR_PARAM_RESET =									"0"	#All attributes off
_CSI_SGR_PARAM_BOLD =									"1"	
_CSI_SGR_PARAM_FAINT =									"2"	#Not widely supported
_CSI_SGR_PARAM_ITALIC_ON =								"3"	#Not widely supported, sometimes treated as inverse
_CSI_SGR_PARAM_UNDERLINE_SINGLE =						"4"
_CSI_SGR_PARAM_BLINK_SLOW =							"5"
_CSI_SGR_PARAM_BLINK_RAPID =							"6"
_CSI_SGR_PARAM_IMAGE_NEGATIVE =						"7"	#Inverse or reverse; swap foreground and background.
_CSI_SGR_PARAM_FONT_PRIME =							"10"
_CSI_SGR_PARAM_FONT_ALT_1 =							"11"
_CSI_SGR_PARAM_FONT_ALT_2 =							"12"
_CSI_SGR_PARAM_FONT_ALT_3 =							"13"
_CSI_SGR_PARAM_FONT_ALT_4 =							"14"
_CSI_SGR_PARAM_FONT_ALT_5 =							"15"
_CSI_SGR_PARAM_FONT_ALT_6 =							"16"
_CSI_SGR_PARAM_FONT_ALT_7 =							"17"
_CSI_SGR_PARAM_FONT_ALT_8 =							"18"
_CSI_SGR_PARAM_FONT_ALT_9 =							"19"
_CSI_SGR_PARAM_FONT_NORM_COLOR =						"22"	#Neither bold nor faint
_CSI_SGR_PARAM_NO_ITALIC_NO_FRAKUR =					"23"
_CSI_SGR_PARAM_UNDERLINE_NONE =						"24"	#Not singly or doubly underlined.
_CSI_SGR_PARAM_BLINK_OFF =								"25"
_CSI_SGR_PARAM_IMAGE_POSITIVE =						"27"
_CSI_SGR_PARAM_TEXT_CLR_BLACK =						"30"
_CSI_SGR_PARAM_TEXT_CLR_RED =							"31"
_CSI_SGR_PARAM_TEXT_CLR_GREEN =						"32"
_CSI_SGR_PARAM_TEXT_CLR_YELLOW =						"33"
_CSI_SGR_PARAM_TEXT_CLR_BLUE =							"34"
_CSI_SGR_PARAM_TEXT_CLR_MAGENTA =						"35"
_CSI_SGR_PARAM_TEXT_CLR_CYAN =							"36"
_CSI_SGR_PARAM_TEXT_CLR_WHITE =						"37"
_CSI_SGR_PARAM_TEXT_CLR_DEFAULT =						"39"
_CSI_SGR_PARAM_BG_CLR_BLACK =							"40"
_CSI_SGR_PARAM_BG_CLR_RED =							"41"
_CSI_SGR_PARAM_BG_CLR_GREEN =							"42"
_CSI_SGR_PARAM_BG_CLR_YELLOW =							"43"
_CSI_SGR_PARAM_BG_CLR_BLUE =							"44"
_CSI_SGR_PARAM_BG_CLR_MAGENTA =						"45"
_CSI_SGR_PARAM_BG_CLR_CYAN =							"46"
_CSI_SGR_PARAM_BG_CLR_WHITE =							"47"
_CSI_SGR_PARAM_BG_CLR_DEFAULT =						"49"

_CSI_DSR = _CSI + "6" + "n" #Reports the cursor position to the application as (as though typed at the keyboard) ESC[n;mR, where n is the row and m is the column. (May not work on MS-DOS.)
_CSI_SCP = _CSI + "s" #Save cursor position
_CSI_RCP = _CSI + "u" #Restores the cursor position
_CSI_CUHIDE = _CSI + "?25!"	#Hides the cursor (trailing character is lowercase L.)
_CSI_CUSHOW = _CSI + "?25h"	#Shows the cursor



_CSI_UTIL_CLR_DEFAULT =	_CSI_SGR(_CSI_SGR_PARAM_TEXT_CLR_DEFAULT)
_CSI_UTIL_CLR_BLACK =		_CSI_SGR(_CSI_SGR_PARAM_TEXT_CLR_BLACK)
_CSI_UTIL_CLR_RED =		_CSI_SGR(_CSI_SGR_PARAM_TEXT_CLR_RED)
_CSI_UTIL_CLR_GREEN =		_CSI_SGR(_CSI_SGR_PARAM_TEXT_CLR_GREEN)
_CSI_UTIL_CLR_YELLOW =		_CSI_SGR(_CSI_SGR_PARAM_TEXT_CLR_YELLOW)
_CSI_UTIL_CLR_BLUE =		_CSI_SGR(_CSI_SGR_PARAM_TEXT_CLR_BLUE)
_CSI_UTIL_CLR_MAGENTA =	_CSI_SGR(_CSI_SGR_PARAM_TEXT_CLR_MAGENTA)
_CSI_UTIL_CLR_CYAN =		_CSI_SGR(_CSI_SGR_PARAM_TEXT_CLR_CYAN)
_CSI_UTIL_CLR_WHITE =		_CSI_SGR(_CSI_SGR_PARAM_TEXT_CLR_WHITE)

_CSI_UTIL_CLR_BLACK_BOLD = 		_CSI_SGR(_CSI_SGR_PARAM_TEXT_CLR_BLACK + ';' + _CSI_SGR_PARAM_BOLD)
_CSI_UTIL_CLR_RED_BOLD =		_CSI_SGR(_CSI_SGR_PARAM_TEXT_CLR_RED + ';' + _CSI_SGR_PARAM_BOLD)
_CSI_UTIL_CLR_GREEN_BOLD =		_CSI_SGR(_CSI_SGR_PARAM_TEXT_CLR_GREEN + ';' + _CSI_SGR_PARAM_BOLD)
_CSI_UTIL_CLR_YELLOW_BOLD =	_CSI_SGR(_CSI_SGR_PARAM_TEXT_CLR_YELLOW + ';' + _CSI_SGR_PARAM_BOLD)
_CSI_UTIL_CLR_BLUE_BOLD =		_CSI_SGR(_CSI_SGR_PARAM_TEXT_CLR_BLUE + ';' + _CSI_SGR_PARAM_BOLD)
_CSI_UTIL_CLR_MAGENTA_BOLD =	_CSI_SGR(_CSI_SGR_PARAM_TEXT_CLR_MAGENTA + ';' + _CSI_SGR_PARAM_BOLD)
_CSI_UTIL_CLR_CYAN_BOLD =		_CSI_SGR(_CSI_SGR_PARAM_TEXT_CLR_CYAN + ';' + _CSI_SGR_PARAM_BOLD)
_CSI_UTIL_CLR_WHITE_BOLD =		_CSI_SGR(_CSI_SGR_PARAM_TEXT_CLR_WHITE + ';' + _CSI_SGR_PARAM_BOLD)
_CSI_UTIL_BOLD =		_CSI_SGR(_CSI_SGR_PARAM_BOLD)
_CSI_UTIL_RESET =				_CSI_SGR(_CSI_SGR_PARAM_RESET)

def _CSI_STR_BLACK(str): return "%s%s%s" % (  _CSI_UTIL_CLR_BLACK, str, _CSI_UTIL_RESET )
def _CSI_STR_RED(str): return "%s%s%s" % (    _CSI_UTIL_CLR_RED, str, _CSI_UTIL_RESET )
def _CSI_STR_GREEN(str): return "%s%s%s" % (  _CSI_UTIL_CLR_GREEN, str, _CSI_UTIL_RESET )
def _CSI_STR_YELLOW(str): return "%s%s%s" % ( _CSI_UTIL_CLR_YELLOW, str, _CSI_UTIL_RESET )
def _CSI_STR_BLUE(str): return "%s%s%s" % (   _CSI_UTIL_CLR_BLUE, str, _CSI_UTIL_RESET )
def _CSI_STR_MAGNET(str): return "%s%s%s" % ( _CSI_UTIL_CLR_MAGENT, str, _CSI_UTIL_RESET )
def _CSI_STR_CYAN(str): return "%s%s%s" % (   _CSI_UTIL_CLR_CYAN, str, _CSI_UTIL_RESET )
def _CSI_STR_WHITE(str): return "%s%s%s" % (  _CSI_UTIL_CLR_WHITE, str, _CSI_UTIL_RESET )

def _CSI_STR_BLACK_BOLD(str): return "%s%s%s" % (  _CSI_UTIL_CLR_BLACK_BOLD, str, _CSI_UTIL_RESET )
def _CSI_STR_RED_BOLD(str): return "%s%s%s" % (    _CSI_UTIL_CLR_RED_BOLD, str, _CSI_UTIL_RESET )
def _CSI_STR_GREEN_BOLD(str): return "%s%s%s" % (  _CSI_UTIL_CLR_GREEN_BOLD, str, _CSI_UTIL_RESET )
def _CSI_STR_YELLOW_BOLD(str): return "%s%s%s" % ( _CSI_UTIL_CLR_YELLOW_BOLD, str, _CSI_UTIL_RESET )
def _CSI_STR_BLUE_BOLD(str): return "%s%s%s" % (   _CSI_UTIL_CLR_BLUE_BOLD, str, _CSI_UTIL_RESET )
def _CSI_STR_MAGNET_BOLD(str): return "%s%s%s" % ( _CSI_UTIL_CLR_MAGENT_BOLD, str, _CSI_UTIL_RESET )
def _CSI_STR_CYAN_BOLD(str): return "%s%s%s" % (   _CSI_UTIL_CLR_CYAN_BOLD, str, _CSI_UTIL_RESET )
def _CSI_STR_WHITE_BOLD(str): return "%s%s%s" % (  _CSI_UTIL_CLR_WHITE_BOLD, str, _CSI_UTIL_RESET )


default = _CSI_UTIL_CLR_DEFAULT
black =   _CSI_UTIL_CLR_BLACK
red =     _CSI_UTIL_CLR_RED
green =  _CSI_UTIL_CLR_GREEN
yellow =  _CSI_UTIL_CLR_YELLOW
blue =    _CSI_UTIL_CLR_BLUE
magenta = _CSI_UTIL_CLR_MAGENTA
cyan =    _CSI_UTIL_CLR_CYAN
white =   _CSI_UTIL_CLR_WHITE

black_bold =   _CSI_UTIL_CLR_BLACK_BOLD
red_bold =     _CSI_UTIL_CLR_RED_BOLD
green_bold =  _CSI_UTIL_CLR_GREEN_BOLD
yellow_bold =  _CSI_UTIL_CLR_YELLOW_BOLD
blue_bold =    _CSI_UTIL_CLR_BLUE_BOLD
magenta_bold = _CSI_UTIL_CLR_MAGENTA_BOLD
cyan_bold =    _CSI_UTIL_CLR_CYAN_BOLD
white_bold =   _CSI_UTIL_CLR_WHITE_BOLD

def clrprint(s, clr):
  print "%s%s%s" % (clr, s, _CSI_UTIL_RESET);

def clrstr(s, clr):
  return "%s%s%s" % (clr, s, _CSI_UTIL_RESET);

###########################################################################################################
def test():
  clrprint("Red", red);
  print clrstr("Blue", blue);

if __name__ == "__main__":
  test();
