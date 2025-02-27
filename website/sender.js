function send_message() {
    var string = document.getElementById("message").value;
    var msg = {
        "string": string,
    }
    localStorage.setItem("message", JSON.stringify(msg));

    console.log(msg);
//ajax
fetch("http://localhost:8000/receive_message"), {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({msg}),
}
.then(response => {
    if (!response.ok) {
        throw new Error("response was not ok");
    }
    return response.json()
})
    .then(data => {
        console.log("data from server: ", data)
    })
    .catch(error => {
        console.log("something went wrong with the response", error);
    });
}
