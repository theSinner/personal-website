(function () {
  "use strict";
})();
module.exports = function (grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON("package.json"),

    notify: {
      task_name: {
        options: {
          // Task-specific options go here.
        },
      },
      sassed: {
        options: {
          title: "Task Complete", // optional
          message: "SASSed!", //required
        },
      },
      server: {
        options: {
          message: "Server is ready!",
        },
      },
    },
    compass: {
      dist: {
        options: {
          sassDir: "static/scss",
          cssDir: "static/css",
          environment: "development",
          outputStyle: "compressed",
        },
      },
    },

    watch: {
      files: [
        "&lt;%= jshint.files %&gt;",
        "static/scss/**/*.scss",
        "static/scss/**/*.css",
      ],
      tasks: ["compass", "notify:sassed"],
    },
  });
  grunt.loadNpmTasks("grunt-notify");
  grunt.loadNpmTasks("grunt-contrib-concat");
  grunt.loadNpmTasks("grunt-contrib-jshint");
  grunt.loadNpmTasks("grunt-contrib-compass");
  grunt.loadNpmTasks("grunt-contrib-watch");
  grunt.registerTask("default", ["compass", "notify:sassed", "watch"]);
};
