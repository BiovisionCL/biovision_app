
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import '../../features/home/presentation/home_page.dart';
import '../../features/about/presentation/about_page.dart';
import '../../features/services/presentation/services_page.dart';
import '../../features/contact/presentation/contact_page.dart';

final GoRouter appRouter = GoRouter(
  routes: [
    GoRoute(path: '/', builder: (context, state) => HomePage()),
    GoRoute(path: '/contact', builder: (context, state) => ContactPage()),
    GoRoute(path: '/services', builder: (context, state) => ServicesPage()),
    GoRoute(path: '/about', builder: (context, state) => AboutPage()),
  ],
);
