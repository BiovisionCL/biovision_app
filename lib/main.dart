import 'package:flutter/material.dart';
// import 'package:firebase_core/firebase_core.dart';
import 'router/app_router.dart';
import 'core/theme/app_theme.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
//   await Firebase.initializeApp();
  runApp(const BiovisionApp());
}

class BiovisionApp extends StatelessWidget {
  const BiovisionApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      debugShowCheckedModeBanner: false,
      title: 'Biovision',
      theme: AppTheme.lightTheme,
      routerConfig: AppRouter.router,
    );
  }
}