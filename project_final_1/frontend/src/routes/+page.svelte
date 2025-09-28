<script lang="ts">
  import Papa from "papaparse";
  import { Chart, type ChartConfiguration, registerables } from "chart.js";
  import csvFile from "../../../data/cluster_data.csv?raw";
  import { writable } from "svelte/store";

  interface Data {
    Clusters_agg: number;
    poverty_2020: number;
    region: string;
  }

  const csvData = writable<Data[]>([]);
  Chart.register(...registerables);
  let canvas: HTMLCanvasElement;
  let chart: Chart;

  function createChart() {
    const config: ChartConfiguration = {
      type: "bar",
      data: {
        labels: $csvData.map((data) => data.region),
        datasets: [
          {
            label: "Уровень бедности",
            data: $csvData.map((data) => data.poverty_2020),
            backgroundColor: "rgba(54, 162, 235, 0.8)",
            borderColor: "rgba(54, 162, 235, 1)",
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            display: true,
          },
        },
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    };

    chart = new Chart(canvas, config);
  }

  $effect(() => {
    Papa.parse<Data>(csvFile, {
      complete: function (results) {
        csvData.set(results.data.filter((data) => data.Clusters_agg === 3));
      },
      header: true,
      skipEmptyLines: true,
      dynamicTyping: true,
      transform: (value) => value.trim(),
    });

    createChart();
  });
</script>

<h1>Топ бедных регионов Российской федерации</h1>

<div class="chart-container">
  <canvas bind:this={canvas}></canvas>
</div>

<style>
  .chart-container {
    position: relative;
    height: 400px;
    width: 100%;
  }
</style>
