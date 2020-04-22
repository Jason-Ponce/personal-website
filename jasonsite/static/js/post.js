document.addEventListener("DOMContentLoaded", skillImageReplacer);

function skillImageReplacer() {
    const skillList = document.getElementsByClassName("post-skill")
    for(var i = 0; i < skillList.length; i++){
        const skillItem = skillList[i].innerText;
        switch(skillItem){
            case 'Python':
                const pythonSrc = '\\static\\images\\pills\\SVG\\python_pills.svg';
                const pythonImg = imgBuilder(pythonSrc);
                var tagId = getId(skillList[i]);
                tagId.innerText = '';
                tagId.appendChild(pythonImg);
                break;
            case 'Flask':
                const flaskSrc = '\\static\\images\\pills\\SVG\\flask_pills.svg';
                const flaskImg = imgBuilder(flaskSrc);
                var tagId = getId(skillList[i]);
                tagId.innerText = '';
                tagId.appendChild(flaskImg);
                break;
            case 'HTML':
                const htmlSrc = '\\static\\images\\pills\\SVG\\html_pills.svg';
                const htmlImg = imgBuilder(htmlSrc);
                var tagId = getId(skillList[i]);
                tagId.innerText = '';
                tagId.appendChild(htmlImg);          
                break;
            case 'Javascript':
                const javascriptSrc = '\\static\\images\\pills\\SVG\\javascript_pills.svg';
                const javascriptImg = imgBuilder(javascriptSrc);
                var tagId = getId(skillList[i]);
                tagId.innerText = '';
                tagId.appendChild(javascriptImg);
                break;
            case 'React':
                const reactSrc = '\\static\\images\\pills\\SVG\\react_pills.svg';
                const reactImg = imgBuilder(reactSrc);
                var tagId = getId(skillList[i]);
                tagId.innerText = '';
                tagId.appendChild(reactImg);
                break;
            case 'PHP':
                const phpSrc = '\\static\\images\\pills\\SVG\\php_pills.svg';
                const phpImg = imgBuilder(phpSrc);
                var tagId = getId(skillList[i]);
                tagId.innerText = '';
                tagId.appendChild(phpImg);
                break;
            case 'CSS':
                const cssSrc = '\\static\\images\\pills\\SVG\\css_pills.svg';
                const cssImg = imgBuilder(cssSrc);
                var tagId = getId(skillList[i]);
                tagId.innerText = '';
                tagId.appendChild(cssImg);
                break;

        }
    }
}

function imgBuilder(source){
    var img = new Image(90, 45);
    img.src = source;
    return img;
}

function getId(obj){
    const eleId = obj.id; 
    const queryPointer = document.getElementById(eleId);
    return queryPointer;
}
