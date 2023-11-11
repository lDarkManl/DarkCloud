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

function changeOrderOnRandom(){
	head = document.querySelector('.head-cards');
	children = head.children;
	[...children].sort(() => Math.random() - 0.5).forEach(v => head.append(v));
}

function makeCheckboxes(){
	let head = document.querySelector('.form-cards');
	let headCards = document.querySelector('.head-cards');
	let title = document.querySelector('.title');
	if (head.firstElementChild)
	{
		head.innerHTML = '';
		headCards.style.display = 'block';
		title.style.display = 'none';
	}
	else
	{	
		headCards.style.display = 'none';
		for(let card of headCards.children)
		{
			let newInput = document.createElement("input");
			newInput.type = 'checkbox';
			newInput.name = 'card';
			newInput.className = 'form-check-input';
			newInput.value = `${card.firstElementChild.innerHTML};${card.lastElementChild.innerHTML}`;

			let cloneCard = card.cloneNode(true);

			let divWrapper = document.createElement("div");
			divWrapper.className = 'form-check head-cards';
			divWrapper.appendChild(newInput);
			divWrapper.appendChild(cloneCard);

			parent = document.querySelector('.form-cards');
			parent.appendChild(divWrapper);
		}
		title.style.display = 'block';
		let newButton = document.createElement('button');
		newButton.innerHTML = 'Перенести';
		newButton.type = 'submit';
		newButton.id = 'button-submit';
		head.appendChild(newButton);
	}
	
}

function changeCard(elem){
	if (elem.className == 'card-front')
	{
		elem.className = 'card-back';
		back = elem.nextElementSibling;
		let temp = elem.innerHTML;
		elem.innerHTML = back.innerHTML;
		back.innerHTML = temp;
		back.className = 'span-front';
	}
	else
	{
		elem.className = 'card-front';
		back = elem.nextElementSibling;
		let temp = elem.innerHTML;
		elem.innerHTML = back.innerHTML;
		back.innerHTML = temp;
		back.className = 'span-back';
	}
}