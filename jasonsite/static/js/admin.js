//resets new user form
function resetInput(){
    document.getElementById("user_name").resetInput();
    window.location.reload();

}

function unhideTag(el){
    const str_tag = 'tag_block'
    const id_str = el.id.slice(3,4)
    var id_num = parseInt(id_str) 
    id_num += 1
    const tag_id = str_tag.concat(String(id_num))
    const target_el = document.getElementById(tag_id)
    console.log(target_el)
    target_el.style.display = 'block';
    target_el.style.visibility = 'visible';
}

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.autocomplete_tags');
    var instances = M.Autocomplete.init(elems, {
        data:{
            "Python": null,
            "JavaScript": null,
            "CSS": null,
            "HTML": null,
            "HTML5": null,
            "Flask": null,
            "AWS": null,
            "React": null,
            "PHP": null,
        }
    });
});
