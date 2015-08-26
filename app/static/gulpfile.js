var gulp = require('gulp')

var jshint = require('gulp-jshint');
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');

// Compile bootstrap sass
gulp.task('bs_sass', function() {
    return gulp.src('bower_components/bootstrap-sass/assets/stylesheets/scout_bs.scss')
    .pipe(sass())
    .pipe(gulp.dest('assets/css'));
});

// Simple move of the bootstrap js to assets.
gulp.task('bs_js', function() {
    return gulp.src('bower_components/bootstrap-sass/assets/javascripts/bootstrap.min.js')
    .pipe(gulp.dest('assets/js'));
});

// Watch Files For Changes
gulp.task('watch', function() {
    gulp.watch('bower_components/bootstrap-sass/assets/stylesheets/scout_bs.scss', ['bs_sass']);
});

gulp.task('default', ['bs_sass', 'bs_js', 'watch']);