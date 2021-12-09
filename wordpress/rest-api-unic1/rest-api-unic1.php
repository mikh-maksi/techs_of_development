<?php


 /**
 * Plugin Name: Unic
 * Description: Плагин для создания собственного REST API
 */

 // создание маршрута
add_action( 'rest_api_init', function(){

	// пространство имен
	$namespace = 'unic/v1';

	// маршрут
	$rout = '/author-posts/(?P<id>\d+)';

	// параметры конечной точки (маршрута)
	$rout_params = [
		'methods'  => 'GET',
		'callback' => 'my_awesome_func1',
		'args'     => [
			'arg_str' => [
				'type'     => 'string', // значение параметра должно быть строкой
				'required' => false,     // параметр обязательный
				'default' => '1', 
			],
			'id' => [
				'type'    => 'integer', // значение параметра должно быть числом
				'default' => 1,        // значение по умолчанию = 10
			],
		],
		'permission_callback' => function( $request ){
			// только авторизованный юзер имеет доступ к эндпоинту
			return 1;
		},
	];

	register_rest_route( $namespace, $rout, $rout_params );

} );

// функция обработчик конечной точки (маршрута)
function my_awesome_func1( WP_REST_Request $request ){
	$fp = fopen('log.txt', 'w');
	$mytext = "Working\n";
	$test = fwrite($fp, $mytext);
	fclose($fp);

	$posts = get_posts( [
		'author' => (int) $request['id'],
	] );

	if ( empty( $posts ) ) {
		return new WP_Error( 'no_author_posts', 'No posts found', [ 'status' => 404 ] );
	}

	return $posts;
}