document.addEventListener("DOMContentLoaded", skillImageReplacer);

function skillImageReplacer() {
    const skillList = document.getElementsByClassName("post-skill")
    for(var i = 0; i < skillList.length; i++){
        const skillItem = skillList[i].innerText;
        switch(skillItem){
            case 'Python':
                const pythonSrc = '\\static\\images\\pills\\python_pills.png';
                const pythonImg = imgBuilderPill(pythonSrc);
                var tagId = getId(skillList[i]);
                tagId.innerText = '';
                tagId.appendChild(pythonImg);
                break;
            case 'Flask':
                const flaskSrc = '\\static\\images\\pills\\flask_pills.png';
                const flaskImg = imgBuilderPill(flaskSrc);
                var tagId = getId(skillList[i]);
                tagId.innerText = '';
                tagId.appendChild(flaskImg);
                break;
            case 'HTML':
                const htmlSrc = '\\static\\images\\pills\\html_pills.png';
                const htmlImg = imgBuilderShield(htmlSrc);
                var tagId = getId(skillList[i]);
                tagId.innerText = '';
                tagId.appendChild(htmlImg);          
                break;
            case 'JavaScript':
                const javascriptSrc = '\\static\\images\\pills\\javascript_pills.png';
                const javascriptImg = imgBuilderShield(javascriptSrc);
                var tagId = getId(skillList[i]);
                tagId.innerText = '';
                tagId.appendChild(javascriptImg);
                break;
            case 'React':
                const reactSrc = '\\static\\images\\pills\\react_pills.png';
                const reactImg = imgBuilderPill(reactSrc);
                var tagId = getId(skillList[i]);
                tagId.innerText = '';
                tagId.appendChild(reactImg);
                break;
            case 'PHP':
                const phpSrc = '\\static\\images\\pills\\php_pills.png';
                const phpImg = imgBuilderPill(phpSrc);
                var tagId = getId(skillList[i]);
                tagId.innerText = '';
                tagId.appendChild(phpImg);
                break;
            case 'CSS':
                const cssSrc = '\\static\\images\\pills\\css_pills.png';
                const cssImg = imgBuilderShield(cssSrc);
                var tagId = getId(skillList[i]);
                tagId.innerText = '';
                tagId.appendChild(cssImg);
                break;

        }
    }
}

function imgBuilderPill(source){
    var img = new Image(95, 35);
    img.src = source;
    return img;
}

function imgBuilderShield(source){
    var img = new Image(55, 55);
    img.src = source;
    img.className = 'shield';
    return img;
}

function getId(obj){
    const eleId = obj.id; 
    const queryPointer = document.getElementById(eleId);
    return queryPointer;
}
