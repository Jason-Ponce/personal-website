
function unhideEl(el){
    let parent = document.getElementById(el.id).parentNode;
    let parent_id_name = parent.id;
    let id_name = parent_id_name.slice(0,parent_id_name.length -1);
    let id_num_str = parent_id_name.slice(parent_id_name.length -1);
    let id_num = parseInt(id_num_str); 
    id_num +=1;
    const next_child_id = id_name.concat(String(id_num));
    const target_next_child_id = document.getElementById(next_child_id);
    target_next_child_id.style.display = 'block';
    target_next_child_id.style.visibility = 'visible';
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