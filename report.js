google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawBasic);

function drawBasic() {

      var data = google.visualization.arrayToDataTable([['orders_count', 'customers_count'], ['1', 11], ['2', 9], ['3', 10], ['4', 8], ['5+', 9]]);

      var options = {
        title: 'Customer distribution',
        
        hAxis: {
          title: 'Number of customers',
          minValue: 0
        },
        vAxis: {
          title: 'Number of orders'
        }
      };

      var chart = new google.visualization.BarChart(document.getElementById('chart_div'));

      chart.draw(data, options);
}