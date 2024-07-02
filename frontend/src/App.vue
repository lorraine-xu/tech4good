<template>
  <div id="app">
    <div class="container">
      <div class="left-side">
        <PdfUploader @file-loaded="handleFileLoaded" />
      </div>
      <div class="right-side">
        <PdfViewer v-if="pdfData" :pdfData="pdfData" />
      </div>
    </div>
  </div>
</template>

<script>
import PdfUploader from "./components/PdfUploader.vue";
import PdfViewer from "./components/PdfViewer.vue";

export default {
  components: {
    PdfUploader,
    PdfViewer
  },
  data() {
    return {
      pdfData: null
    };
  },
  methods: {
    handleFileLoaded(data) {
      this.pdfData = data;
    }
  }
};
</script>

<style>
#app {
  text-align: center;
  margin-top: 50px;
}

.container {
  display: flex;
  height: 100vh;
}

.left-side, .right-side {
  flex: 1;
}

.left-side {
  background-color: #f0f0f0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.right-side {
  background-color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>