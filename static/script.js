document.addEventListener("DOMContentLoaded", function () {
    const candidates = [
        { id: 1, name: "Candidate A" },
        { id: 2, name: "Candidate B" },
        { id: 3, name: "Candidate C" }
        // Add more candidates as needed
    ];

    const candidatesContainer = document.querySelector(".candidates");
    const voteButton = document.getElementById("castVote");
    const messageElement = document.getElementById("message");

    // Create candidate radio buttons dynamically
    candidates.forEach((candidate) => {
        const label = document.createElement("label");
        label.innerHTML = `
            <input type="radio" name="candidate" value="${candidate.id}">
            ${candidate.name}
        `;
        candidatesContainer.appendChild(label);
    });

    // Event listener for casting a vote
    voteButton.addEventListener("click", function () {
        const selectedCandidate = document.querySelector('input[name="candidate"]:checked');

        if (!selectedCandidate) {
            showMessage("Please select a candidate to cast your vote.");
        } else {
            const candidateId = selectedCandidate.value;
            // Send the vote to the server (you need to implement this)
            // Display a success message or handle errors accordingly
            showMessage(`You voted for Candidate ${candidateId}.`);
        }
    });

    // Function to display a message to the user
    function showMessage(message) {
        messageElement.textContent = message;
        setTimeout(() => {
            messageElement.textContent = "";
        }, 5000); // Clear the message after 5 seconds
    }
});
