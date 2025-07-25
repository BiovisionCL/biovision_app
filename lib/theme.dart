import 'package:flutter/material.dart';

class AppColors {
  static const primary = Color(0xFF0B3D91);
  static const secondary = Color(0xFFC5A880);
  static const background = Colors.white;
  static const textPrimary = Colors.black87;
  static const textSecondary = Colors.black54;
}

class AppTextStyles {
  static const headline1 = TextStyle(fontSize: 32, fontWeight: FontWeight.bold, fontFamily: 'Merriweather', color: AppColors.primary);
  static const headline6 = TextStyle(fontSize: 20, fontWeight: FontWeight.w600, color: AppColors.textPrimary);
  static const bodyText1 = TextStyle(fontSize: 16, color: AppColors.textPrimary);
  static const bodyText2 = TextStyle(fontSize: 14, color: AppColors.textSecondary);
  static const button = TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.white);
}

final ThemeData appTheme = ThemeData(
  brightness: Brightness.light,
  primaryColor: AppColors.primary,
  scaffoldBackgroundColor: AppColors.background,
  colorScheme: ColorScheme.fromSwatch().copyWith(secondary: AppColors.secondary),
  fontFamily: 'Lato',
  textTheme: TextTheme(
    displayLarge: AppTextStyles.headline1,
    titleLarge: AppTextStyles.headline6,
    bodyLarge: AppTextStyles.bodyText1,
    bodyMedium: AppTextStyles.bodyText2,
    labelLarge: AppTextStyles.button,
  ),
  elevatedButtonTheme: ElevatedButtonThemeData(
    style: ElevatedButton.styleFrom(
      backgroundColor: AppColors.primary,
      foregroundColor: Colors.white,
      padding: EdgeInsets.symmetric(horizontal: 24, vertical: 12),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
      elevation: 4,
      shadowColor: Colors.black26,
      textStyle: AppTextStyles.button,
    ),
  ),
  appBarTheme: AppBarTheme(
    backgroundColor: AppColors.background,
    elevation: 0,
    iconTheme: IconThemeData(color: AppColors.primary),
    titleTextStyle: AppTextStyles.headline1,
  ),
);
