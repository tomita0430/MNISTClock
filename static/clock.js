function updateClock() {
    const now = new Date();
    const hours = now.getHours();
    const minutes = now.getMinutes();
    const seconds = now.getSeconds();

    document.getElementById('hour-ten').src = `/mnist/${Math.floor(hours / 10)}`;
    document.getElementById('hour-one').src = `/mnist/${hours % 10}`;
    document.getElementById('minute-ten').src = `/mnist/${Math.floor(minutes / 10)}`;
    document.getElementById('minute-one').src = `/mnist/${minutes % 10}`;
    document.getElementById('second-ten').src = `/mnist/${Math.floor(seconds / 10)}`;
    document.getElementById('second-one').src = `/mnist/${seconds % 10}`;
}

setInterval(updateClock, 1000);
updateClock();
