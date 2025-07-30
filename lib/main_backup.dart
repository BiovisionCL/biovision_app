import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'core/widgets/navbar.dart';
import 'core/widgets/footer.dart';
import 'features/home/presentation/home_page.dart';

void main() {
  runApp(const RazonbillApp());
}

class RazonbillApp extends StatelessWidget {
  const RazonbillApp({super.key});

  @override
  Widget build(BuildContext context) {
    final _router = GoRouter(
      initialLocation: '/',
      routes: [
        GoRoute(
          path: '/',
          builder: (context, state) => const HomePage(),
        ),
      ],
    );

    return MaterialApp.router(
      title: 'Razonbill',
      theme: ThemeData(
        fontFamily: 'Roboto',
        brightness: Brightness.light,
        useMaterial3: true,
      ),
      routerConfig: _router,
      debugShowCheckedModeBanner: false,
    );
  }
}