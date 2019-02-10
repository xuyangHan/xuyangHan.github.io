/* Set the width of the side navigation to 250px and the left margin of the page content to 250px */
function openQueryBar() {
    document.getElementById("mySidenav").style.width = "500px";
    document.getElementById("main").style.marginLeft = "500px";
    document.getElementById("sidebaropenbtn").innerHTML = '<i class="fas fa-angle-double-left"></i>';
    document.getElementById("sidebaropenbtn").onclick = closeQueryBar;
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0 */
function closeQueryBar() {
    document.getElementById("mySidenav").style.width = "0%";
    document.getElementById("main").style.marginLeft = "0%";
    document.getElementById("sidebaropenbtn").onclick = openQueryBar;
    document.getElementById("sidebaropenbtn").innerHTML = '<i class="fas fa-angle-double-right"></i>';
}

mapboxgl.accessToken = 'pk.eyJ1IjoiamF5a2Fyb255b3JrIiwiYSI6ImNqa2JjZzNkeTA5ZGkzcG55OXhmcnZxMTIifQ.XotoTIdsT-bYoQpodyW3xg';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v9',
    center: [-96, 37.8],
    zoom: 3
});

/* Dash Modal */
// Get the button that opens the modal
let modal_btn = document.getElementById("modal-Btn");

// Get the modal
let dash_modal = document.getElementById('dash-Modal');

// Get the <span> element that closes the modal
let modal_close_span = document.getElementById("dash-Modal-close");

// When the user clicks the button, open the modal
modal_btn.onclick = function () {
    dash_modal.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
modal_close_span.onclick = function () {
    dash_modal.style.display = "none";
};


/* Dash Help Modal */
// Get the button that opens the modal
let dash_tip_btn = document.getElementById("dash-tip");

// Get the modal
let dash_help_modal = document.getElementById('dash-help-Modal');

// Get the <span> element that closes the modal
let dash_help_modal_close_span = document.getElementById("dash-help-Modal-close");

// When the user clicks the button, open the modal
dash_tip_btn.onclick = function () {
    dash_help_modal.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
dash_help_modal_close_span.onclick = function () {
    dash_help_modal.style.display = "none";
};


/* Query Help Modal */
// Get the button that opens the modal
let query_tip_btn = document.getElementById("query-tip");

// Get the modal
let query_help_modal = document.getElementById('query-help-Modal');

// Get the <span> element that closes the modal
let query_help_modal_close_span = document.getElementById("query-Modal-close");

// When the user clicks the button, open the modal
query_tip_btn.onclick = function () {
    query_help_modal.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
query_help_modal_close_span.onclick = function () {
    query_help_modal.style.display = "none";
};


function openQueryContent(evt, searchType) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("query-tab-content");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tab-links");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(searchType).style.display = "block";
    evt.currentTarget.className += " active";
}

// Get the element with id="defaultChecked" and check it
document.getElementById("defaultChecked").checked = true;


function closeResults() {
    document.getElementById("query-section").style.display = "block";
    document.getElementById("data-list-section").style.display = "none";
    document.getElementById("data-detail").style.display = "none";
    document.getElementById("resultsopenbtn").innerHTML = '<p>Go to Data Records &nbsp; </p><i class="fas fa-caret-right"></i>';
    document.getElementById("resultsopenbtn").onclick = openResults;
    document.getElementById("myInput").value = '';
    e = $.Event('keyup');
    e.keyCode = 13; // enter
    $('input').trigger(e);
}

function openResults() {
    document.getElementById("query-section").style.display = "none";
    document.getElementById("data-list-section").style.display = "block";
    document.getElementById("data-detail").style.display = "none";
    document.getElementById("resultsopenbtn").innerHTML = ' <i class="fas fa-caret-left"></i> &nbsp; <p>Back to Search Type</p>';
    document.getElementById("resultsopenbtn").onclick = closeResults;
}


$(document).ready(function () {
    $("#myInput").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#datasets li").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
        $("#query-section li").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});

function openDataDetails() {
    document.getElementById("query-section").style.display = "none";
    document.getElementById("data-list-section").style.display = "none";
    document.getElementById("data-detail").style.display = "block";
    document.getElementById("resultsopenbtn").innerHTML = '<i class="fas fa-caret-left"></i><p> &nbsp; Back to Data Records</p>';
    document.getElementById("resultsopenbtn").onclick = openResults;
}

$('#search-by-uploader li').on('click', function (e) {
    let element = e.target.id;
    openResults();
    document.getElementById("myInput").value = element;

    e = $.Event('keyup');
    e.keyCode = 13; // enter
    $('input').trigger(e);
});


function addDataLayer() {
    document.getElementById("delete-layer-btn").disabled = false;
    document.getElementById("add-layer-btn").disabled = true;
    let myDiv = document.getElementById("my-datasets");
    let node = document.createElement("li");
    let textnode = document.createTextNode('10/12/2018 - 10/12/2018 CIDCO ');
    node.appendChild(textnode);
    let iconnode = document.createElement("i");
    iconnode.onclick = deleteLayer;
    iconnode.className = "fas fa-trash-alt";
    node.appendChild(iconnode);
    node.className = "is-hoverable";
    node.id = "my-data-cidco";
    node.onclick = openDataDetails;
    myDiv.appendChild(node);
    // myDiv.appendChild('<li class="is-hoverable" id="my-data-cidco"><span onclick="openDataDetails()">'
    //     + '10/12/2018 - 10/12/2018 CIDCO '
    //     + '</span> <i class="fas fa-trash-alt" onclick="deleteLayer()"></i></li>');
    check_mydatalayer();
}

function deleteLayer() {
    document.getElementById("delete-layer-btn").disabled = true;
    document.getElementById("add-layer-btn").disabled = false;
    document.getElementById("my-data-cidco").remove();
    check_mydatalayer();

}

function check_mydatalayer() {
    let div_mydatalist = document.getElementById("my-datasets");
    let number_mydatalayer = div_mydatalist.getElementsByTagName("li").length;
    if (number_mydatalayer <= 1) {
        document.getElementById("no-layer-selected").style.display = "block";
    } else {
        document.getElementById("no-layer-selected").style.display = "none";
    }
}
