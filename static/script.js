function rewrite(){
	content=this.innerHTML;
	area = document.getElementById('textareainput');
	area.innerHTML = content;
	this.id = '';
	area.id = '';

}

function giveId(){
	this.id = 'textinput';
	this.previousSibling.lastChild.id = 'textareainput';
}