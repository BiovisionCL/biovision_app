import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../features/home/presentation/home_page.dart';

class AppRouter {
  static final GoRouter router = GoRouter(
    routes: [
      GoRoute(
        path: '/',
        builder: (context, state) => const HomePage(),
      ),
    ],
  );
}