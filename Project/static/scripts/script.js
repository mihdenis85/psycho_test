"use strict";

function unfade(obj) {
	var op = 0.01;
	var timer = setInterval(function () {
	    if (op >= 1){
	        clearInterval(timer);
	    }
	    obj.style.opacity = op;
	    op += 0.02;
	}, 10);
}

function fade(obj) {
	var op = 0.99;
	var timer = setInterval(function () {
	    if (op <= 0){
	        clearInterval(timer);
	    }
	    obj.style.opacity = op;
	    op -= 0.02;
	}, 10);
}

function new_style(obj, style) {
	obj.style = style;
}

function menu_in() {
	var style = `border-radius: 30px;
	border-color: #fbbb81;
	background-color: #fbbb81;
	color: black;
	padding-top: 10px;
	padding-bottom: 10px;
	padding-left: 25px;
	padding-right: 25px;`;
	fade(this);
	setTimeout(new_style, 500, this, style);
	setTimeout(unfade, 500, this);
};

function menu_out() {
	var style = `color: white;
	padding-top: 10px;
	padding-bottom: 10px;
	padding-left: 25px;
	padding-right: 25px;`;
	fade(this);
	setTimeout(new_style, 500, this, style);
	setTimeout(unfade, 500, this);
};


menu_button_1.onmouseover = menu_in;
menu_button_1.onmouseout = menu_out;
menu_button_2.onmouseover = menu_in;
menu_button_2.onmouseout = menu_out;
menu_button_3.onmouseover = menu_in;
menu_button_3.onmouseout = menu_out;
menu_button_4.onmouseover = menu_in;
menu_button_4.onmouseout = menu_out;