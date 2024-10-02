const colors = {
    "W": "rgb(249, 250, 244)",
    "U": "rgb(14, 104, 171)",
    "B": "rgb(21, 11, 0)",
    "R": "rgb(211, 32, 42)",
    "G": "rgb(0, 115, 62)"
}

function updateDisplay(player_number, commander1, commander2) {
    // Initialize to start
    if(["p1", "p4"].indexOf(player_number) > -1) {
        document.getElementById(player_number).style.paddingRight = "";
    } else {
        document.getElementById(player_number).style.paddingLeft = "";
    }
    document.getElementById(player_number).style.background = "transparent";
    document.getElementById(player_number+"-title").style.width = "";

    if (commander1.name && commander2.name) {
        document.getElementById(player_number + "-title").innerHTML = commander1.name + "<br>" + commander2.name;
    } else if (commander1.name) {
        document.getElementById(player_number + "-title").innerHTML = commander1.name;
    } else if (commander2.name) {
        document.getElementById(player_number + "-title").innerHTML = commander2.name;
    } else {
        document.getElementById(player_number + "-title").innerHTML = "";
        document.getElementById(player_number + "-title").style.width = "";
        document.getElementById(player_number).style.background = "transparent";
        return;
    }

    let width = document.getElementById(player_number).offsetWidth;
    document.getElementById(player_number+"-title").style.width = (width * 1.1) + "px";
    if(["p1", "p4"].indexOf(player_number) > -1) {
        document.getElementById(player_number).style.paddingRight = (width * .1) + "px";
    } else {
        document.getElementById(player_number).style.paddingLeft = (width * .1) + "px";
    }
    
    let color_identity = commander1.colors + commander2.colors;
    let gradient_colors = [];
    Object.keys(colors).forEach(color => {
        if(color_identity.indexOf(color) > -1) {
            gradient_colors.push(colors[color]);
        }
    });

    document.getElementById(player_number).style.background = 
        gradient_colors.length > 1 ? "linear-gradient(180deg, " + gradient_colors.join(", ") + ")" : gradient_colors[0];
}

function loadCommanders(raw_data) {
    return {
        "p1": {
            "commander1": {
                "name": raw_data.player1_commander1 !== null ? raw_data.player1_commander1 : "",
                "colors": raw_data.player1_commander1_ci !== null ? raw_data.player1_commander1_ci.split(',') : []
            },
            "commander2": {
                "name": raw_data.player1_commander2 !== null ? raw_data.player1_commander2 : "",
                "colors": raw_data.player1_commander2_ci !== null ? raw_data.player1_commander2_ci.split(',') : []
            }
        },
        "p2": {
            "commander1": {
                "name": raw_data.player2_commander1 !== null ? raw_data.player2_commander1 : "",
                "colors": raw_data.player2_commander1_ci !== null ? raw_data.player2_commander1_ci.split(',') : []
            },
            "commander2": {
                "name": raw_data.player2_commander2 !== null ? raw_data.player2_commander2 : "",
                "colors": raw_data.player2_commander2_ci !== null ? raw_data.player2_commander2_ci.split(',') : []
            }
        },
        "p3": {
            "commander1": {
                "name": raw_data.player3_commander1 !== null ? raw_data.player3_commander1 : "",
                "colors": raw_data.player3_commander1_ci !== null ? raw_data.player3_commander1_ci.split(',') : []
            },
            "commander2": {
                "name": raw_data.player3_commander2 !== null ? raw_data.player3_commander2 : "",
                "colors": raw_data.player3_commander2_ci !== null ? raw_data.player3_commander2_ci.split(',') : []
            }
        },
        "p4": {
            "commander1": {
                "name": raw_data.player4_commander1 !== null ? raw_data.player4_commander1 : "",
                "colors": raw_data.player4_commander1_ci !== null ? raw_data.player4_commander1_ci.split(',') : []
            },
            "commander2": {
                "name": raw_data.player4_commander2 !== null ? raw_data.player4_commander2 : "",
                "colors": raw_data.player4_commander2_ci !== null ? raw_data.player4_commander2_ci.split(',') : []
            }
        }
    };
}

export { updateDisplay, loadCommanders };