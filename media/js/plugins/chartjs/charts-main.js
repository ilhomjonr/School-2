// Bar chart

new Chart($("#chart_1"), {
    type: 'bar',
    data: {
        labels: [
            "Янв",
            "Фев",
            "Мар",
            "Апр",
            "Май",
            "Июн",
            "Июл",
            "Авг",
            "Сен",
            "Окт",
            "Ноя",
            "Дек"
        ],
        datasets: [{
            data: [25, 40, 22, 12, 57, 20, 5, 15, 38, 20, 70, 35],
            backgroundColor: "#cfd6e1",
            hoverBackgroundColor: "#8696b4"
        }]
    },
    options: {
        legend: {
            display: false
        },
        scales: {
            xAxes: [{
                gridLines: {
                    display:false
                },
                categoryPercentage: 0.97,
                barPercentage: 0.97
            }],
            yAxes: [{
                gridLines: {
                    display:false
                },
                ticks:{
                    callback: function(value) {
                        if(value != 0) {
                            return value + ' ч';
                        }
                    }
                }
            }]
        },
        tooltips: {
            custom: function(tooltip) {
                if (!tooltip) return;
                tooltip.displayColors = false;
            },
            callbacks: {
                label: function(tooltipItem, data) {
                    return tooltipItem.yLabel + " часов";
                }
            }
        }
    }
});

// Doughnut chart
new Chart($("#chart_2"), {
    type: 'doughnut',
    data: {
        labels: [
            "Маркетинг",
            "Экономика",
            "Инностраные языки",
            "Менеджемент",
            "Политика Узбекистана"
        ],
        datasets: [{
            data: [15, 5, 12, 8, 20],
            backgroundColor: [
                "#3498DB",
                "#9B59B6",
                "#E74C3C",
                "#26B99A",
                "#F2C94C"
            ]
        }]
    },
    options: {
        responsive: false,
        legend: {
            display: false
        },
        tooltips: {
            custom: function(tooltip) {
                if (!tooltip) return;
                tooltip.displayColors = false;
            }
        }
    }
});