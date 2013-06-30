window.onload = function(){
    // get tab container
    var container = document.getElementById("tab-container"),
        tabcon    = document.getElementById("tab-contents"),
        navitem   = document.getElementById("tabHeader_1");

    // store which tab we are on
    var ident = navitem.id.split("_")[1];
    navitem.parentNode.setAttribute("data-current", ident);

    // set current tab with class of ActiveTabHeader
    navitem.classList.add("tabActiveHeader");

    // hide tab contents we don't need
    var pages = tabcon.getElementsByClassName("tabpage");
    for (var i = 1; i < pages.length; i++) {
        pages.item(i).style.display = "none";
    }

    // add click event to tabs
    var tabs = container.getElementsByClassName("tabdiv");
    for (var i = 0; i < tabs.length; i++) {
        tabs[i].onclick = displayPage;
    }    
}

function displayPage(){
    var current = this.parentNode.getAttribute("data-current");

    // remove class of activeTabHeader and hide old contents
    document.getElementById("tabHeader_" + current).classList.remove("tabActiveHeader");
    $("#tabpage_" + current).hide();

    var ident = this.id.split("_")[1];

    // add class of activeTabHeader to new active tab and show contents
    this.classList.add("tabActiveHeader");
    document.getElementById("tabpage_" + ident).style.display = "block";
    this.parentNode.setAttribute("data-current", ident);
}