<template>
    <div>
      <div v-for="pageNum in numPages" :key="pageNum">
        <canvas :ref="setCanvasRef(pageNum)"></canvas>
      </div>
    </div>
  </template>
  
  <script>
  import * as pdfjsLib from "pdfjs-dist/webpack";
  import "pdfjs-dist/web/pdf_viewer.css";
  
  export default {
    props: {
      pdfData: ArrayBuffer
    },
    data() {
      return {
        numPages: 0,
        canvasRefs: []
      };
    },
    watch: {
      pdfData: "renderPdf"
    },
    methods: {
      setCanvasRef(pageNum) {
        return (el) => {
          this.canvasRefs[pageNum - 1] = el;
        };
      },
      async renderPdf() {
        const pdf = await pdfjsLib.getDocument(this.pdfData).promise;
        this.numPages = pdf.numPages;
  
        for (let pageNum = 1; pageNum <= this.numPages; pageNum++) {
          const page = await pdf.getPage(pageNum);
          const viewport = page.getViewport({ scale: 1.5 });
          const canvas = this.canvasRefs[pageNum - 1];
          const context = canvas.getContext("2d");
          canvas.height = viewport.height;
          canvas.width = viewport.width;
          page.render({ canvasContext: context, viewport: viewport });
        }
      }
    }
  };
  </script>