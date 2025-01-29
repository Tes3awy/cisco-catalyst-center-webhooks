function scheduleNextCheck() {
    setTimeout(checkServerStatus, 5000);
}
async function checkServerStatus() {
    const statusIndicator = document.getElementById('status-indicator');
    const status = document.getElementById('status');
    try {
        const response = await fetch('/server-status');
        if (response.ok && response.status === 200) {
            const data = await response.json();
            console.log(`[${new Date().toLocaleTimeString()}] Server Status:`, data.status);
            if (data.status === "up" && !status.classList.contains("text-green")) {
                status.textContent = "Up";
                status.classList.add("text-green");
                status.classList.remove("text-red");
                statusIndicator.classList.add("status-green");
                statusIndicator.classList.remove("status-red");
            } else if (data.status === "down" && !status.classList.contains("text-red")) {
                status.textContent = "Down";
                status.classList.add("text-red");
                status.classList.remove("text-green");
                statusIndicator.classList.add("status-red");
                statusIndicator.classList.remove("status-green");
            }
        } else {
            throw new Error("Server responded with an erroneous status");
        }
    } catch (error) {
        console.error(`[${new Date().toLocaleTimeString()}] Server Status: Down`);
        console.error("Error fetching server status:", error);
        if (!status.classList.contains("text-red")) {
            status.textContent = "DOWN (Fetch Failed)!";
            status.classList.add("text-red");
            status.classList.remove("text-green");
            statusIndicator.classList.add("status-red");
            statusIndicator.classList.remove("status-green");
        }
    }
    scheduleNextCheck();
}
