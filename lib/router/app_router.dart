import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../features/home/presentation/home_page.dart';
import '../features/about/about_page.dart';
import '../features/services/services_page.dart';
import '../features/contact/contact_page.dart';
import '../features/login/login_page.dart';

class AppRouter {
  static final GoRouter router = GoRouter(
    routes: [
      GoRoute(
        path: '/',
        builder: (context, state) => const HomePage(),
      ),
      GoRoute(
        path: '/quienes-somos',
        builder: (context, state) => const AboutPage(),
      ),
      GoRoute(
        path: '/servicios',
        builder: (context, state) => const ServicesPage(),
      ),
      GoRoute(
        path: '/contacto',
        builder: (context, state) => const ContactPage(),
      ),
      GoRoute(
        path: '/login',
        builder: (context, state) => const LoginPage(),
      ),
    ],
  );
}