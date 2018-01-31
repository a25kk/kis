import gulp from 'gulp';
import del from 'del';

var cfg = require('./../config.json');

// 1. Cleaning tasks
gulp.task('clean:dist', del.bind(null, [cfg.paths.dist]));
gulp.task('clean:assets', del.bind(null, ['.tmp', cfg.paths.dist + 'assets']));
gulp.task('clean:metadata', del.bind(null, ['src/.jekyll-metadata'], {dot: true}));
