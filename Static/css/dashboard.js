console.log("js is working");
//sidebar close-open functionality

var sidebarOpen = false;

function toggleSidebar() {
    if (!sidebarOpen) {
        document.getElementById("sidebar").classList.add("sidebar_responsive");
        sidebarOpen = true;
    }
}

function closeSidebar() {
   if (sidebarOpen){
       document.getElementById("sidebar").classList.remove("sidebar_responsive");
       sidebarOpen = false;
   }
}