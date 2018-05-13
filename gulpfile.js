const gulp = require('gulp');
const sass = require('gulp-sass');

// Compile and Sass & Inject Into Browser

gulp.task('sass', function(){
	return gulp.src(['node_modules/bootstrap/scss/bootstrap.scss', 'static/scss/*.scss'])
		.pipe(sass())
		.pipe(gulp.dest("static/css"))
});

// Move JS Files to src/js
gulp.task('js', function(){
	return gulp.src(['node_modules/bootstrap/dist/js/bootstrap.min.js', 'node_modules/jquery/dist/jquery.min.js', 'node_modules/popper.js/dist/umd/popper.min.js'])
		.pipe(gulp.dest("static/js"))
});

// Move fonts folder to src/fonts
gulp.task('fonts', function(){
	return gulp.src('node_modules/font-awesome/fonts/*')
		.pipe(gulp.dest("static/fonts"));
});


// Move Font Awesome CSS to src/css
gulp.task('fa', function(){
	return gulp.src('node_modules/font-awesome/css/font-awesome.min.css')
		.pipe(gulp.dest("static/css"));
});

// When we run Gulp, these are what will be ran
gulp.task('default', ['sass', 'js', 'fa', 'fonts']);