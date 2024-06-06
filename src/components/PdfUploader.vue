<template>
    <div>
      <input type="file" accept="application/pdf" @change="onFileChange" />
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      onFileChange(event) {
        const file = event.target.files[0];
        if (file && file.type === "application/pdf") {
          const reader = new FileReader();
          reader.onload = (e) => {
            this.$emit('file-loaded', e.target.result);
          };
          reader.readAsArrayBuffer(file);
        } else {
          alert("Please upload a PDF file.");
        }
      }
    }
  };
  </script>