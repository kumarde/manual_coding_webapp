document.addEventListener("DOMContentLoaded", function(event) {
    var requests = '{{requests}}'
    
    function getNewRequest(){
        var nextString = requests.pop();
        document.getElementById("tweet_text").innerHTML = nextString;
    }
    
    getNewRequest();
});
