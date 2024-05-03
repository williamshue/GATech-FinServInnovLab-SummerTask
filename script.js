// Load the JSON data from the file
d3.json("dummy_data.json").then(data => {
    // Set up the SVG dimensions and margins
    const margin = { top: 20, right: 20, bottom: 30, left: 50 };
    const width = 600 - margin.left - margin.right;
    const height = 400 - margin.top - margin.bottom;
  
    // Create the SVG container
    const svg = d3.select("#chart")
      .append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", `translate(${margin.left},${margin.top})`);
  
    // Create scales for x and y axes
    const xScale = d3.scaleBand()
      .range([0, width])
      .domain(Object.keys(data.C1))
      .padding(0.1);
  
    const yScale = d3.scaleLinear()
      .range([height, 0])
      .domain([0, d3.max(Object.values(data.C1), d => parseFloat(d.stock_price.replace("$", "")))]);
  
    // Create x and y axes
    const xAxis = d3.axisBottom(xScale);
    const yAxis = d3.axisLeft(yScale);
  
    // Append x and y axes to the SVG
    svg.append("g")
      .attr("transform", `translate(0,${height})`)
      .call(xAxis);
  
    svg.append("g")
      .call(yAxis);
  
    // Create line generators for each company
    const line = d3.line()
      .x(d => xScale(d[0]))
      .y(d => yScale(parseFloat(d[1].stock_price.replace("$", ""))));
  
    // Append lines for each company
    Object.entries(data).forEach(([company, companyData]) => {
      svg.append("path")
        .datum(Object.entries(companyData))
        .attr("fill", "none")
        .attr("stroke", company === "C1" ? "steelblue" : "orange")
        .attr("stroke-width", 1.5)
        .attr("d", line);
    });
  
    // Create a tooltip div
    const tooltip = d3.select("body")
      .append("div")
      .attr("class", "tooltip")
      .style("opacity", 0);
  
    // Add hover event listeners to the SVG
    svg.selectAll("path")
      .on("mouseover", (event, d) => {
        const [year, yearData] = d[0];
        tooltip.transition()
          .duration(200)
          .style("opacity", 0.9);
        tooltip.html(`<strong>Year: ${year}</strong><br>${yearData.text}`)
          .style("left", `${event.pageX}px`)
          .style("top", `${event.pageY - 28}px`);
      })
      .on("mouseout", () => {
        tooltip.transition()
          .duration(500)
          .style("opacity", 0);
      });
  });